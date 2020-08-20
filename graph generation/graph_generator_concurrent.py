import csv
import sys
start = 500#int(sys.argv[1])
end = 6000#int(sys.argv[2])
import numpy as np

labels = ['landing page',              #0
          'application landing page',  #1
          'application login page',    #2
          'contact check',             #3
          'getThanas',                 #4
          'getColleges',               #5
          'getCollegeSVG',             #6
          'final application submission',#7
          'full application process'   #8
         ]

def appending(metrics, indices, splitted_line):
    i = 0
    for metric in metrics:
        index = indices[i]
        i += 1
        metric.append(splitted_line[index])
'''
csvfile = open('/Users/tariqadnan/Desktop/2020 Data/Concurrent/combined_summary.csv', 'a+')
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(['Request Lables','Concurrency Level', 
                    'Error %', 'Average', 'Median', 
                    '90th Pct', '95th Pct', '99th Pct'
                ])

for rate in np.arange(start, end+1, 500):
    fname = '/Users/tariqadnan/Desktop/2020 Data/Concurrent/Finished Applications/concurrent_summary_'+str(rate)+'.csv'
    f = open(fname, 'r')
    lines = []
    error = []         #3
    average = []       #4
    median = []         #7
    Pct_90 = []  #8
    Pct_95 = []  #9
    Pct_99 = []  #10

    metrics = [error, average, median, Pct_90, Pct_95, Pct_99]

    indices = [3,4,7,8,9,10]

    for line_no in range(37):
        lines.append(f.readline()[:-1])

    #landing page
    splitted_line = lines[1].split(',')
    appending(metrics, indices, splitted_line)
    
    
    #app landing page
    splitted_line = lines[2].split(',')
    appending(metrics, indices, splitted_line)

    
    #app login page
    splitted_line = lines[3].split(',')
    appending(metrics, indices, splitted_line)

    #contact check
    splitted_line = lines[4].split(',')
    appending(metrics, indices, splitted_line)
    
    #get thanas
    splitted_line_1 = [0]*len(splitted_line)
    for j in [5,21,26,29]:
        splitted_line = lines[j].split(',')
        for index in indices:
            splitted_line_1[index] += float(splitted_line[index])
    splitted_line_1 = [round(number / 4,2) for number in splitted_line_1]
    appending(metrics, indices, splitted_line_1)

    #get colleges
    splitted_line_1 = [0]*len(splitted_line)
    for j in [6, 7, 11, 15, 17, 19, 22, 23, 27, 29, 30, 31, 33]:
        splitted_line = lines[j].split(',')
        for index in indices:
            splitted_line_1[index] += float(splitted_line[index])
    splitted_line_1 = [round(number / 13,2) for number in splitted_line_1]
    appending(metrics, indices, splitted_line_1)

    #get colleges svg
    splitted_line_1 = [0]*len(splitted_line)
    for j in [9-1, 10-1, 11-1, 13-1, 14-1, 15-1, 17-1, 19-1, 21-1, 25-1, 29-1, 33-1, 35-1]:
        splitted_line = lines[j].split(',')
        for index in indices:
            splitted_line_1[index] += float(splitted_line[index])
    splitted_line_1 = [round(number / 13 ,2) for number in splitted_line_1]
    appending(metrics, indices, splitted_line_1)

    #final submission
    splitted_line = lines[35].split(',')
    appending(metrics, indices, splitted_line)

    #full application submission
    splitted_line = lines[36].split(',')
    appending(metrics, indices, splitted_line)
    
    i = 0
    for label in labels:
        csvwriter.writerow([label,rate, 
                    error[i], average[i], median[i], 
                    Pct_90[i], Pct_95[i], Pct_99[i]
                ])
        i += 1


csvfile.close()

'''
raw_file = open('/Users/tariqadnan/Downloads/Association%20for%20Computing%20Machinery%20(ACM)%20-%20SIG%20Proceedings%20Template/graph generation/combined_summary_final.csv', 'r')
lines = raw_file.readlines()

raw_file = open('/Users/tariqadnan/Downloads/Association%20for%20Computing%20Machinery%20(ACM)%20-%20SIG%20Proceedings%20Template/graph generation/combined_summary_test.csv', 'r')
lines_test = raw_file.readlines()

lines = lines[1:]
lines_test = lines_test[1:]

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
metric = ['Error', 'Average', 'Median', '90th Pct', '95th Pct', '99th Pct']
req = ['Thana Retrieval', 'College Retrieval', 'College SVG Retrieval','Application Submission', 'Full Application']
marker = ['.','*','x','X','p','8']
def draw(http_request, index, lines):
    x = []
    y = []
    for i in range(0,int(len(lines)/len(req))):
        splitted_line = lines[i*len(req)+http_request].split(',')
        x.append(int(splitted_line[1]))
        y.append(float(splitted_line[index]))
    return x,y



indices = [2,3,4,5,6,7]
figure(num=None, figsize=(9, 6), dpi=150, facecolor='w', edgecolor='k')
g_type = 0

for i in range(0,len(req)-1):
    x,y = draw(i, indices[g_type], lines_test)
    plt.plot(x,y,label=req[i]+' (Test Bed)',marker=marker[i], color='#2276ca')
for i in range(0,len(req)-1):
    x,y = draw(i, indices[g_type], lines)
    plt.plot(x,y,label=req[i]+' (Final Env)',marker=marker[i],color='g')
plt.xlabel('Concurrency',fontsize=14)
ylabel = metric[g_type]+' Rate In Percentage'
plt.ylabel(ylabel,fontsize=14)
plt.legend(fontsize=12, loc='best')
plt.xticks([100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000],['','','','','','','',''],fontsize=14) 
plt.yticks(fontsize=14) 
#plt.show()
plt.savefig(ylabel+'.pdf',format='pdf') 
plt.close()

for g_type in range (1,6):
    figure(num=None, figsize=(9, 6), dpi=150, facecolor='w', edgecolor='k')
    for i in range(0,len(req)-1):
        x,y = draw(i, indices[g_type], lines_test)
        plt.plot(x,y,label=req[i]+' (Test Bed)',marker=marker[i], color='#2276ca')
    for i in range(0,len(req)-1):
        x,y = draw(i, indices[g_type], lines)
        plt.plot(x,y,label=req[i]+' (Final Env)',marker=marker[i],color='g')
    plt.xlabel('Concurrency',fontsize=14)
    ylabel = metric[g_type]+' Response Time In ms'
    plt.ylabel(ylabel,fontsize=14)
    plt.legend(fontsize=12, loc='best')
    plt.xticks([100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000],['','','','','','','',''],fontsize=14) 
    plt.yticks(fontsize=14) 
    #plt.show()
    plt.savefig(ylabel+'.pdf',format='pdf') 
    plt.close()

figure(num=None, figsize=(9, 6), dpi=150, facecolor='w', edgecolor='k')
for g_type in range (1,6):
    x,y = draw(http_request=4,index=indices[g_type],lines=lines_test)
    plt.plot(x,y,label=metric[g_type]+' (Test Bed)',marker=marker[g_type],color='#2276ca')
for g_type in range (1,6):
    x,y = draw(http_request=4,index=indices[g_type],lines=lines)
    plt.plot(x,y,label=metric[g_type]+' (Final Env)',marker=marker[g_type],color='g')
plt.xlabel('Concurrency',fontsize=14)
ylabel ='Response Time In ms'
plt.ylabel(ylabel,fontsize=14)
plt.legend(fontsize=12, loc='best')
plt.xticks([100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000],['','','','','','','',''],fontsize=14) 
plt.yticks(fontsize=14) 
#plt.show()
plt.savefig('Full Application '+ylabel+'.pdf',format='pdf') 
plt.close()
