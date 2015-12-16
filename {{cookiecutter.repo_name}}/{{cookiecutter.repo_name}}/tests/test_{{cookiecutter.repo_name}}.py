#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

import random
import pytest



class Test{{ cookiecutter.repo_name|capitalize }}(unittest.TestCase):

    @pytest.fixture(params=[2, 3])
    def static_data(self, request):
        return [random.randint() for _ in range(request.param)]

    def test_something(self):
        from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}
        pass


if __name__ == '__main__':
    unittest.main()
