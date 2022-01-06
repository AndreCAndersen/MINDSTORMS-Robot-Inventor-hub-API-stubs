import json
import os

TYPE_MAPPING = {
    "String": "str",
    "Integer": "int",
    "Float": "float",
    "Boolean": "bool",
    "Any type": "Any",
    "Callable function": "Callable",
}


class DocsBuilder:

    def __init__(
        self,
        input_file='lego_ms_docs.json',
        output_file='lego_ms_docs.md',
        verbose=False,
    ):
        self.input_file = input_file
        self.output_file = output_file
        self.verbose = verbose
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def write_article(self, article, depth):
        for content in article['content']:
            self.write("# " + content['article_title'])
            for subcontent in content['content']:
                if 'article' in subcontent:
                    self.write_article(subcontent['article'], depth + 1)
                if 'text' in subcontent:
                    self.write(subcontent['text']['content'])
                if 'python_method_description' in subcontent:
                    for python_code_example in subcontent['python_method_description']['content']:
                        self.write(python_code_example['description'])
                        for code_example in python_code_example['code_example']:
                            self.write_code(code_example)
                        self.write_method(
                            python_code_example['description'],
                            python_code_example['python_method_description_title'],
                            python_code_example['parameters'],
                            python_code_example['code_example'],
                        )
                if 'python_code_example' in subcontent:
                    for code_example in subcontent['python_code_example']['content']:
                        self.write_code(code_example)

    def get_only_code(self, code_examples):
        code = ''
        for code_example in code_examples:
            code += code_example['code']
            for idx, comment in enumerate(code_example['comments']):
                code = code.replace('Comment{}'.format(idx + 1), comment['comment'])
        return code

    def write_code(self, code_example):
        self.write("### " + code_example['title'].split('-')[-1])
        code = '\n```python\n' + code_example['code'] + '\n```\n'
        for idx, comment in enumerate(code_example['comments']):
            code = code.replace('Comment{}'.format(idx + 1), comment['comment'])
        self.write(code)

    def write_method(
        self,
        description,
        title,
        parameters,
        code_examples
    ):
        docs = ''
        value_asserts = []
        param_strings = ['self']
        for parameter in parameters:
            param_string = parameter['parameter_title']
            param_string += ': ' + TYPE_MAPPING[parameter['type']]
            if parameter['default']:
                param_string += ' = ' + parameter['default']
            parameter_description = ' '.join(parameter['description'].split())
            docs += f":param {parameter['parameter_title']}: {parameter_description}\n"
            value_asserts.append((parameter['parameter_title'], parameter['values']))
            param_strings.append(param_string)
        param_strings = ', '.join(param_strings)
        if description:
            description = description.replace('\n', '\n        ')
            description = description.strip()
        if code_examples:
            code = self.get_only_code(code_examples)
            code = "        Example:\n\n            " + code.replace('\n', '\n            ').rstrip() + '\n'
        else:
            code = ""
        if docs:
            if description:
                description += description + '\n'
            docs = docs.replace('\n', '\n        ')
            docs = f'"""{description}\n{code}\n        {docs}"""'
            docs = "    " + docs.strip()
        else:
            docs = f'    """{description}\n{code}        """'
        code_content = ''
        for var, val in value_asserts:
            if ' to ' in val:
                val = val.split(' to ')
                code_content += f'        assert {val[0]} <= {var} <= {val[1]}\n'
            elif ' - ' in val:
                val = val.split(' - ')
                code_content += f'        assert {val[0]} <= {var} <= {val[1]}\n'
            elif ('"' in val or "'" in val) and ',' in val:
                val = val.replace(',  ', ', ')
                code_content += f'        assert {var} in [{val}]\n'
            elif '-' in val:
                val = val.split('-')
                code_content += f'        assert {val[0]} <= {var} <= {val[1]}\n'
            elif 'True or False' == val:
                code_content += f'        assert isinstance({var}, bool)\n'
            elif not val:
                pass
            else:
                code_content += f'\n        assert {var} = {val}\n'
        if not code_content:
            code_content = '        pass\n'
        code = f'```python\n    def {title}({param_strings}):\n    {docs}\n{code_content}```\n\n'

        # TODO: Write docs about possible exceptions.

        self.write(code)

    def write_docs(self):
        with open(self.input_file, encoding='utf8') as file:
            docs = json.load(file)
            contents = docs["content"]
            for content1 in contents:
                if 'text' in content1:
                    self.write(content1['text']['content'])
                if 'article' in content1:
                    self.write_article(content1['article'], 0)

    def write(self, text):
        if self.verbose:
            print(text)
        with open(self.output_file, 'at', encoding='utf8') as file:
            file.write(text + '\n')


if __name__ == '__main__':
    builder = DocsBuilder(verbose=True)
    builder.write_docs()
