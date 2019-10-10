import textfsm

fp = './RET_WULTE_JLJATIDUA_TB_XXX.csv'
template = './TEMPLATE_RET.tmplt'

with open(fp) as f:
    data = f.read()
    # print(data)


    print('--------------RESULT')
    with open(template) as t:
        re_table = textfsm.TextFSM(t)
        fsm_results = re_table.ParseText(data)

        print(re_table.header)

        for row in fsm_results:
            print(row)