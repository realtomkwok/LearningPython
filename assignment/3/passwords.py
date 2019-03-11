passwords = ['shen502', 'd270476', '760430fox', '1214oo', 'maik68755', 'newrj0', 'telnet1', 'hans72', 's12345',
             'zhii971', 'zyf600690', 'han6736', 'Rocke', 'ifuckyouESRT$%', 'zfj93363211', 'yuanji12', '1234abc',
             'tide9999', 'aaa1', 'yeef1234', 'lj7202', 'ts5022', 'wxq123', 'Helena', 'lsh705', 'zhy1428', 'By1The',
             'KIC43dk6!', 'www.lIve.01', '6crx99tj', 'fxmfxm88', 'Piggy_02', 'ABab12', 'shen1208', 'wt99lqq', 'liu0615',
             'Swhy920520', 'snmp2000', 'f0411701', 'dhj4pjq', '168zlp', 'shy75723', 'Pas@123e', 'O0O0OO0.Com',
             '67617yxb', '99g1', '1981hl82', 'hily9221', 'LiuXingKai_72', 'lxj7544', 'xr818', 'onnihili.m', 'dd350002',
             'm0190', 'cool007', 'edit/p/w', 'passwd102', 'ad0918', 'ly741221', 'zhs123', 'huang513', 'zy780512',
             'Password01!', 'feb2', 'nb701206', 'lqj8575', 'g6j9m8o6', 'f800800', 'without555', 'zhoum163', 'fantacy2',
             'WinDow', 'jjm640426', 'naile72', '990cj7576', 'qaz123m', 'xjtu539', 'wk770630', 'loveyou99', 'fxj102',
             'casper9', 'my1316pass', 'Mylovedn', 'spring1', '520982620a', 'FireTM', 'visualc74', 'smart1010',
             '74110.Net', 'wf1947', 'ghj654321', 'earthworm0316', 'abc123', 'mt1hy9bh', 'zxd25fjkd', 'Gggfhv2008!@',
             'M@bius7089', 'pingsky28skm', 'cced123', 'jeff1234', '1900@csdn', 'YZC116@dmin', 'iscjt1103', '7474liu',
             'cgi123', 'xxm760331', '!QAZxsw2', 'mirandali810813', 'xx1205', 'a13982', '--Ice258--', '820616Wzj@!!',
             "ppnn13%dkstFeb.1st", 'P@ssw0rd']


def filter_passwords(any_arguments_you_need):
    """Please modify this function as necessary"""
    pass


"""
When the filter_passwords function is completed, the following test_filter function should not raise any AssertionError,
which means the program runs as expected.
"""


def test_filter():
    """This is a function to test whether the filter_passwords meets the requirements as specified in the assignment"""
    strong_passwords = filter_passwords(passwords)
    assert strong_passwords == {'74110.Net', 'Gggfhv2008!@', 'LiuXingKai_72', 'O0O0OO0.Com', 'Password01!',
                                '--Ice258--', 'ppnn13%dkstFeb.1st','www.lIve.01', 'KIC43dk6!', 'YZC116@dmin',
                                '820616Wzj@!!', 'Piggy_02', 'M@bius7089', '!QAZxsw2', 'P@ssw0rd', 'Pas@123e'},\
                                "The filtered passwords returned from the filter_passwords function don't " \
                                "match the expected output."
    print("Congratulations! Your filter_passwords function passed the test successfully!")

test_filter()


"""
Bonus (Optional)
The function generate_strong_password generates random strong passwords like the following:
'9rE*r.Epm>0w_=hF;', '1cI:,X)!', '7cH.=Q=B]vRJ8', '6eF@;>@Y4lB!;0', '3sL!cyQ*`L_YGfMf', '8oX/:Ex4'

Again the test_bonus function, when run, should not raise any AssertionError
"""


def generate_strong_password():
    pass


def test_bonus():
    generated_passwords = set(generate_strong_password() for _ in range(1000))
    assert filter_passwords(generated_passwords) == generated_passwords, \
        "Some of the generated passwords aren't strong enough!"
    print("Congratulations, you aced the bonus!")

# test_bonus()