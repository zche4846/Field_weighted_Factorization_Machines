d_index_conv_type = {
    '54337': 'View_Content',
    '54338': 'Purchase',
    '54339': 'Sign_Up',
    '54340': 'Lead'
}
path_data = '../data_cvr3/cvr_imp_20180708_0714_conv_20180708_0720.csv.add_conv_type.thres5.yx'

def split_by_conv_type(path):
    d_index_file = {}
    for index in d_index_conv_type.keys():
        d_index_file[index] = open(path+'.'+d_index_conv_type[index], 'w')
    for line in open(path):
        index = line.strip('\n').split(' ')[-1].split(':')[0]
        d_index_file[index].write(line)
    for index in d_index_file.keys():
        d_index_file[index].close()

split_by_conv_type(path_data)