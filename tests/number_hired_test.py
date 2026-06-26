from number_hired_guiv3 import number_hired
def test_num_items():
    #|---------------------------------------------------ARRANGE---------------------------------------------------|
    expected_err_invalid = "please enter an integer (ie: a number which does not have a decimal part)"
    expected_err_bound_low = "please enter an integer that is more than (or equal to) 1"
    expected_err_bound_high = "please enter an integer that is less than 500."
    expected_input = "thank you"

    #|---------------------------------------------------ACT---------------------------------------------------| 
 
    #|=====Invalid entries=====|
    str_input = number_hired("XLII")
    flt_input = number_hired(12.5)
    
    #|=====Boundary entries=====|
    low_input = number_hired(0)
    hi_input = number_hired(501)
    
    #|=====Expected entries=====|
    exp_inp_low = number_hired(1)
    exp_inp = number_hired(2)
    exp_bnd_hi = number_hired(500)
    exp_inp_hi = number_hired(499)

    #|---------------------------------------------------ASSERT---------------------------------------------------|
    assert str_input == expected_err_invalid
    assert flt_input == expected_err_invalid
    
    assert low_input == expected_err_bound_low
    assert hi_input == expected_err_bound_high

    assert exp_inp == expected_input
    assert exp_inp_low == expected_input
    assert exp_bnd_hi== expected_input
    assert exp_inp_hi == expected_input
    
    print("All tests passed")

