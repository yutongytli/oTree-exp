from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

# class MyPage(Page):
#     form_model = models.Player
#     form_fields = ['donation', 'org', 'email']
#
#     def vars_for_template(self):
        # cmiddle = []
        # biglist = []
        # temp = []
        # org = []
        # des = []

        # for i in range(1, 11):
        #     if self.participant.vars['care_%s' % i] == 1:
        #         clot.append([self.participant.vars['care_%s' % i], i])
        #     elif self.participant.vars['care_%s' % i] == 2:
        #         cmiddle.append([self.participant.vars['care_%s' % i], i])
        #     elif self.participant.vars['care_%s' % i] == 3:
        #         clittle.append([self.participant.vars['care_%s' % i], i])
        #     else:
        #         pass

        # clot = [self.participant.vars['lot1'], self.participant.vars['lot2'], self.participant.vars['lot3']]
        # clittle = [self.participant.vars['little1'], self.participant.vars['little2'], self.participant.vars['little3']]

        # if len(clot) == 0:
        #     if len(cmiddle) == 0 and len(clittle) != 0:
        #         self.player.annotation = 'only group 3'
        #         if len(clittle) <= 3:
        #             temp = random.sample(clittle, len(clittle))
        #         else:
        #             temp = random.sample(clittle, 3)
        #     elif len(cmiddle) != 0 and len(clittle) == 0:
        #         self.player.annotation = 'only group 2'
        #         if len(cmiddle) <= 3:
        #             temp = random.sample(cmiddle, len(cmiddle))
        #         else:
        #             temp = random.sample(cmiddle, 3)
        #     elif len(cmiddle) != 0 and len(clittle) != 0:
        #         self.player.annotation = 'no group 1'
        #         if len(cmiddle)+len(clittle) == 2:
        #             temp += random.sample(cmiddle, 1)
        #             temp += random.sample(clittle, 1)
        #         else:
        #             temp += random.sample(cmiddle, 1)
        #             temp += random.sample(clittle, 1)
        #             temp1 = [i for i in cmiddle if i not in temp]
        #             temp2 = [i for i in clittle if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     else:
        #         self.player.annotation = 'random'
        #         for i in range(1, 11):
        #             biglist.append([self.participant.vars['care_%s' % i], i])
        #         temp = random.sample(biglist, 3)
        # else:
        #     if len(cmiddle) == 0 and len(clittle) != 0:
        #         self.player.annotation = 'no group 2'
        #         if len(clittle)+len(clot) == 2:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(clittle, 1)
        #         else:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(clittle, 1)
        #             temp1 = [i for i in clot if i not in temp]
        #             temp2 = [i for i in clittle if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     elif len(cmiddle) != 0 and len(clittle) == 0:
        #         self.player.annotation = 'no group 3'
        #         if len(cmiddle)+len(clot) == 2:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(cmiddle, 1)
        #         else:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(cmiddle, 1)
        #             temp1 = [i for i in cmiddle if i not in temp]
        #             temp2 = [i for i in clot if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     elif len(cmiddle) != 0 and len(clittle) != 0:
        #         self.player.annotation = 'all groups'
        #         temp += random.sample(clot, 1)
        #         temp += random.sample(clittle, 1)
        #         temp1 = [i for i in clittle if i not in temp]
        #         temp2 = [i for i in clot if i not in temp]
        #         temp += random.sample(temp1 + temp2, 1)
        #     else:
        #         self.player.annotation = 'only group 1'
        #         if len(clot) <= 3:
        #             temp = random.sample(clot, len(clot))
        #         else:
        #             temp = random.sample(clot, 3)

        # if len(temp) == 1:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     org.append(self.player.org_option1)
        #     no = ['1']
        #     des.append(Constants.description[temp[0][1]])
        # elif len(temp) == 2:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     self.player.org_option2 = Constants.organization[temp[1][1]]
        #     org.append(self.player.org_option1)
        #     org.append(self.player.org_option2)
        #     no = ['1', '2']
        #     des.append(Constants.description[temp[0][1]])
        #     des.append(Constants.description[temp[1][1]])
        # else:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     self.player.org_option2 = Constants.organization[temp[1][1]]
        #     self.player.org_option3 = Constants.organization[temp[2][1]]
        #     org.append(self.player.org_option1)
        #     org.append(self.player.org_option2)
        #     org.append(self.player.org_option3)
        #     no = ['1', '2', '3']
        #     des.append(Constants.description[temp[0][1]])
        #     des.append(Constants.description[temp[1][1]])
        #     des.append(Constants.description[temp[2][1]])

        # temp1 = random.choice(clot)
        # temp2 = random.choice(clittle)
        # temp3 = [i for i in clot if i != temp1]
        # temp4 = [i for i in clittle if i != temp2]
        # temp5 = random.choice(temp3 + temp4)
        # if temp5 in clot:
        #     self.player.annotation = '2 lot'
        # else:
        #     self.player.annotation = '2 little'
        #
        # org = [Constants.organization[temp1-1], Constants.organization[temp2-1], Constants.organization[temp5-1]]
        # des = [Constants.description[temp1-1], Constants.description[temp2-1], Constants.description[temp5-1]]
        # no = ['1', '2', '3']
        #
        # self.player.org_option1 = Constants.organization[temp1-1]
        # self.player.org_option2 = Constants.organization[temp2-1]
        # self.player.org_option3 = Constants.organization[temp5-1]

        # mylist = zip(org, des, no)
        #
        # return {'list': mylist}



    # def is_displayed(self):
    #     return self.participant.vars['group'] == '1LD' or self.participant.vars['group'] == '1QD' or \
    #            self.participant.vars['group'] == '1QND' or self.participant.vars['group'] == '2LD' or \
    #            self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
    #            self.participant.vars['group'] == '3LD' or self.participant.vars['group'] == '3QD' or \
    #            self.participant.vars['group'] == '3QND'



# class Results(Page):
#     form_model = models.Player
#     form_fields = ['email']
#
#     def is_displayed(self):
#         return {(self.player.org == 1 or self.player.org == 2 or self.player.org == 3)
#                 and (self.participant.vars['group'] == '1LP' or self.participant.vars['group'] == '1QP' or \
#                self.participant.vars['group'] == '1QNP' or self.participant.vars['group'] == '2LP' or \
#                self.participant.vars['group'] == '2QP' or self.participant.vars['group'] == '2QNP' or \
#                self.participant.vars['group'] == '3LP' or self.participant.vars['group'] == '3QP' or \
#                self.participant.vars['group'] == '3QNP')}

class MyPage(Page):
    form_model = models.Player
    form_fields = ['donation', 'org', 'email']

    def vars_for_template(self):
        org_random = list(random.sample(Constants.organization, 3))
        des_random = [1, 2, 3]
        for i in range(len(Constants.organization)):
            if org_random[0] == Constants.organization[i]:
                des_random[0] = Constants.description[i]
            elif org_random[1] == Constants.organization[i]:
                des_random[1] = Constants.description[i]
            elif org_random[2] == Constants.organization[i]:
                des_random[2] = Constants.description[i]
            else:
                pass
        no = ['1', '2', '3']

        mylist = zip(org_random, des_random, no)

        self.player.org_option1 = org_random[0]
        self.player.org_option2 = org_random[1]
        self.player.org_option3 = org_random[2]

        return {'list': mylist}


page_sequence = [
    MyPage,
    # Results
]
