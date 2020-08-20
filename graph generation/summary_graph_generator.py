from matplotlib import pyplot as plt
import numpy as np
import json
import sys
count = 34#int(sys.argv[1])

#plt.figure(num=None, figsize=(8, 6), dpi=150, facecolor='w', edgecolor='k')
metric = ['Average', 'Median', '95th Percentile', '99th Percentile']
req = ['Application Log In','Contact Check', 'Application Submission', 'Full Application']
marker = ['*','x','.','X']
def draw(http_request, gtype, index, lines):
    x = []
    y = []
    for i in range(0,int(len(lines)/4)):
        splitted_line = lines[i*4+http_request].split('\t')
        x.append(int(splitted_line[1]))
        y.append(float(splitted_line[index]))
    return x,y


raw_file_test = open('/Users/tariqadnan/Downloads/Association%20for%20Computing%20Machinery%20(ACM)%20-%20SIG%20Proceedings%20Template/graph generation/raw_data_test', 'r')
lines_test = raw_file_test.readlines()
raw_file_final = open('/Users/tariqadnan/Downloads/Association%20for%20Computing%20Machinery%20(ACM)%20-%20SIG%20Proceedings%20Template/graph generation/raw_data_final', 'r')
lines_final = raw_file_final.readlines()
'''
print('Choose HTTP Request:\n1. Application Log In\n2. Contact Check\n3. Application Submission\n4. All')
#http_req = int(input())
#http_req -= 1
print('Choose Response Type\n1. Average\n2. Median\n3. 95th Percentile\n4. 99th Percentile')
#g_type = int(input())

index = 5 #g_type = 1

if g_type == 2: #Median
    index = 8
elif g_type == 3: #95th pct
    index = 10
elif g_type == 4: #95th pct
    index = 11
'''
indices = [0,5,8,10,11]

for g_type in [1,2,3,4]:
    index = indices[g_type]
    x,y = draw(3, g_type, index, lines_test)
    plt.plot(x,y,label=metric[g_type-1],marker=marker[g_type-1])
plt.xlabel('Database Size')
ylabel = 'Response Time (ms)'
plt.ylabel(ylabel)
plt.legend()
#plt.xticks(np.arange(0,x[-1]+51000,50000))
plt.yticks()
plt.savefig('test_db.pdf',format='pdf')
plt.close()

for g_type in [1,2,3,4]:
    index = indices[g_type]
    x,y = draw(3, g_type, index, lines_final)
    plt.plot(x,y,label=metric[g_type-1],marker=marker[g_type-1])
plt.xlabel('Database Size')
ylabel = 'Response Time (ms)'
plt.ylabel(ylabel)
plt.legend()
#plt.xticks(np.arange(0,x[-1]+51000,50000))
plt.yticks()
plt.savefig('final_db.pdf',format='pdf')
plt.close()
exit()
x1 = x
x = []
y1 = []
y2 = []
x_v = 0
for i in range(count):
    fname = "/Users/tariqadnan/Desktop/2020 DATA/Result/"+str(i+1)+"/Make_payment_Report/statistics.json"
    with open(fname) as f:
        data = json.load(f)
        y1.append(float(data["Make Payment"]["meanResTime"]))
        y2.append(float(data["Make Payment"]["medianResTime"]))
        x.append(x_v)
        x_v += 20000

plt.plot(x,y1,label="Average Response Time",marker='.')
plt.plot(x,y2,label="Median Response Time",marker='o')
plt.xlabel('Database Size')
ylabel = 'Response Times (ms)'
plt.ylabel(ylabel)
plt.legend()
plt.xticks(np.arange(0,x1[-1]+51000,50000))
plt.yticks()
plt.savefig('Payment_Response_Times.pdf',format='pdf')
plt.close()
'''
if http_req == 3:
    for g_type in [1,2,3,4]:
        index = indices[g_type]
        for i in [0,2,3]:
            x,y = draw(i, g_type, index, lines)
            plt.plot(x,y,label=req[i],marker=marker[i])
        plt.xlabel('Database Size',fontsize=14)
        ylabel = metric[g_type-1]+' Response Time (ms)'
        plt.ylabel(ylabel,fontsize=14)
        plt.legend(fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.savefig(ylabel+'.pdf',format='pdf')
        plt.close()
else:
    x,y = draw(http_req, g_type, index, lines)
    plt.plot(x,y,label=req[http_req],marker='*')
    plt.xlabel('Database Size')
    ylabel = metric[g_type-1]+' Response Time of '
    ylabel += req[http_req]
    plt.ylabel(ylabel)
    plt.savefig(ylabel+'.pdf',format='pdf')
#plt.show()


'''
