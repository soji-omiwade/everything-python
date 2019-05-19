@add_types_validator(int, (int,float), str)
def product_with_check(arg1, arg2, arg3):
    return '{}: {}'.format(arg3, str(arg1 * arg2))
"""above same as: 
product_with_check = add_types_validator(*types)
"""



    # def test_good_input(self):
        # args = 6, 3, 'result'
        # expected_output = 'result: 18'
        # self.assertEqual(product_with_check(*args), expected_output)

    # def test_different_good_input(self):
        # args = 3, 14, 'answer'
        # expected_output = 'answer: 42'
        # self.assertEqual(product_with_check(*args), expected_output)
        
    # def test_bad_input(self):
        # args = 3.3, 14, 'answer'
        # expected_output = 'answer: 42'
        # with self.assertRaises(BadInputError) as err:
            # product_with_check(*args)