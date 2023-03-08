from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import laliga_table
import Load  

options=Options()
options.add_argument("headless")
driver = webdriver.Chrome()

def extract_ga():
        global df,df1
        
        url='https://www.laliga.com/en-GB/stats/laliga-santander/scorers/team/fc-barcelona'
        print("Collecting FC barcelona's goal data")
        driver.get(url)
        driver.maximize_window()
        time.sleep(20)
        npath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a'
        gpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/p'
        mpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[6]/p'
        gpm_path='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[7]/p'
        p_name=[]
        p_goals=[]
        p_matches=[]
        p_gpm=[]

        p_name.append(driver.find_element(By.XPATH,npath).text)
        p_goals.append(driver.find_element(By.XPATH,gpath).text)
        p_gpm.append(driver.find_element(By.XPATH,gpm_path).text)

        for i in range(2,12):
                npath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[3]/a/p'.format(i)
                gpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                gpm_path='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[7]/p'.format(i)
 
                p_name.append(driver.find_element(By.XPATH,npath).text)
                p_goals.append(driver.find_element(By.XPATH,gpath).text)
                p_gpm.append(driver.find_element(By.XPATH,gpm_path).text)
                
                
                
        score=dict(Name =p_name, Goals =p_goals,GPM=p_gpm)
        df = pd.DataFrame.from_dict(score)


        url1='https://www.laliga.com/en-GB/stats/laliga-santander/assists/team/fc-barcelona'
        print("Collecting FC barcelona's assist data")
        driver.get(url1)
        time.sleep(20)
        npath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a/p'
        apath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/p'
        apm='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[7]/p'

        p_name=[]
        p_assist=[]
        p_apm=[]

        p_name.append(driver.find_element(By.XPATH,npath).text)
        p_assist.append(driver.find_element(By.XPATH,apath).text)
        p_apm.append(driver.find_element(By.XPATH,apm).text)


        for i in range(2,14):
                npath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[3]/a/p'.format(i)
                apath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                apm='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[7]/p'.format(i)
    
                p_name.append(driver.find_element(By.XPATH,npath).text)
                p_assist.append(driver.find_element(By.XPATH,apath).text)
                p_apm.append(driver.find_element(By.XPATH,apm).text)


        assist=dict(Name =p_name, Assist =p_assist,APM=p_apm)
        df1 = pd.DataFrame.from_dict(assist)
        
def yellow_red():
        global df2,df3
        url2='https://www.laliga.com/en-GB/stats/laliga-santander/yellow-cards/team/fc-barcelona'
        url3='https://www.laliga.com/en-GB/stats/laliga-santander/red-cards/team/fc-barcelona'
        print("Collecting total number of yellow cards")
        driver.get(url2)
        driver.maximize_window()
        time.sleep(20)
        ypath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a/p'
        rpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a/p'

        ycpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/p'
        rcpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/p'

        y=[]
        r=[]
        yc=[]
        rc=[]
        y.append(driver.find_element(By.XPATH,ypath).text)
        yc.append(driver.find_element(By.XPATH,ycpath).text)
        
        
        for i in range(2,20):
                ypath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[3]/a/p'.format(i)
                ycpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                y.append(driver.find_element(By.XPATH,ypath).text)
                yc.append(driver.find_element(By.XPATH,ycpath).text)
                
        print("Collecting total number of red cards")
        driver.get(url3)
        driver.maximize_window()
        time.sleep(20)
        r.append(driver.find_element(By.XPATH,rpath).text)
        rc.append(driver.find_element(By.XPATH,rcpath).text)
        for i in range(2,6):
                rpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[3]/a/p'.format(i)
                rcpath='/html/body/div[1]/div[6]/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                r.append(driver.find_element(By.XPATH,rpath).text)
                rc.append(driver.find_element(By.XPATH,rcpath).text)
        yellow= dict(Name =y,Yellow_cards=yc)
        red= dict(Name =r,Red_cards=rc)
        df2 = pd.DataFrame.from_dict(yellow)
        df3 = pd.DataFrame.from_dict(red)

def squard_stats():
        global df4
        url4='https://www.laliga.com/en-GB/clubs/fc-barcelona/stats'
        print("Extracting Barca squard stats")
        driver.get(url4)
        driver.maximize_window()
        time.sleep(20)
        npath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[4]/p'
        mipath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[5]/p'
        gpath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[6]/p'
        spath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[7]/p'
        ppath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[3]/p'

        name=[]
        mins=[]
        games=[]
        start=[]
        pos=[]

        name.append(driver.find_element(By.XPATH,npath).text)
        mins.append(driver.find_element(By.XPATH,mipath).text)
        games.append(driver.find_element(By.XPATH,gpath).text)
        start.append(driver.find_element(By.XPATH,spath).text)
        pos.append(driver.find_element(By.XPATH,ppath).text)

        for i in range(2,27):
                npath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[4]/p'.format(i)
                mipath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                gpath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[6]/p'.format(i)
                spath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[7]/p'.format(i)
                ppath='/html/body/div[1]/div[6]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[3]/p'.format(i)
                
                name.append(driver.find_element(By.XPATH,npath).text)
                mins.append(driver.find_element(By.XPATH,mipath).text)
                games.append(driver.find_element(By.XPATH,gpath).text)
                start.append(driver.find_element(By.XPATH,spath).text)
                pos.append(driver.find_element(By.XPATH,ppath).text)
        squard_stat= dict(Name =name,Position=pos,Mins_played=mins,Matchs=games,Start=start)
        df4 = pd.DataFrame.from_dict(squard_stat)
        print(df4.head(5))

def laliga_table():
        global df5
        url5='https://www.laliga.com/en-GB/laliga-santander/standing'
        driver.get(url5)
        driver.maximize_window()
        time.sleep(20)
        print("Extracting laliga table data")
        pos=[]
        tname=[]
        points=[]
        pld=[]
        w=[]
        d=[]
        l=[]
        gf=[]
        ga=[]
        gd=[]
        tpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/p'
        tname.append(driver.find_element(By.XPATH,tpath).text)
        pos.append(1)
        ppath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[3]/p'
        points.append(driver.find_element(By.XPATH,ppath).text)
        mpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[4]/div[1]/div/div/div[4]/p'
        pld.append(driver.find_element(By.XPATH,mpath).text)
        wpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[5]/p'
        w.append(driver.find_element(By.XPATH,wpath).text)
        dpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[6]/p'
        d.append(driver.find_element(By.XPATH,dpath).text)
        lpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[7]/p'
        l.append(driver.find_element(By.XPATH,lpath).text)
        
        for i in range(4,23):
                pos.append(i-2)
                tpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[2]/div[2]/p'.format(i)
                ppath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[3]/p'.format(i)
                mpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[4]/p'.format(i)
                wpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[5]/p'.format(i)
                dpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[6]/p'.format(i)
                lpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[7]/p'.format(i)
                tname.append(driver.find_element(By.XPATH,tpath).text)
                points.append(driver.find_element(By.XPATH,ppath).text)
                pld.append(driver.find_element(By.XPATH,mpath).text)
                w.append(driver.find_element(By.XPATH,wpath).text)
                d.append(driver.find_element(By.XPATH,dpath).text)
                l.append(driver.find_element(By.XPATH,lpath).text)
                
                
                
                
                
        table=dict(Position =pos, Team =tname,Points=points, Matches_played=pld,Win=w,Draw=d,Lost=l)
        df5 = pd.DataFrame.from_dict(table)
        driver.close()



def load_temp():
        print("STORING TEMPORARILY")
        with pd.ExcelWriter('C:/Users/vggan/Desktop/Barca_project/barca_stats.xlsx') as writer:
                df.to_excel(writer, sheet_name='GOALS',index=False)
                df1.to_excel(writer, sheet_name='ASSISTS',index=False)
                df2.to_excel(writer, sheet_name='YELLOW CARDS',index=False)
                df3.to_excel(writer, sheet_name='RED CARDS',index=False)
                df4.to_excel(writer, sheet_name='SUARD STATS',index=False)
                df5.to_excel(writer, sheet_name='LALIGA TABLE',index=False)
                


if __name__ == '__main__':
        extract_ga()
        yellow_red()
        squard_stats()
        laliga_table()
        load_temp()
        Load.upload()
        #driver.close()
        
