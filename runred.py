#!/usr/bin/env python

#import all necessary packages
import pandas as pd
import click



@click.command()
@click.argument('f', type=click.Path(exists=True))
def cli(f):
        """This is a function that takes a file path of Harvard Registry Export Data and segregates it based on entry,
        i.e Registration, Baseline, Follow-up, Surgery, and Hospitalization databases."""
        #read database into dataframe
        df = pd.read_csv(f)
        #df = pd.read_csv('/Users/snappergoldenhelix/Desktop/Code/REDCAP/REDCap_Harvard_Registry_Export.csv')

        #create Registration Dataframe
        reg = df.ix[df.ix[:,1] == 'Registration Visit']
        reg = reg.drop(reg.columns[30:693], axis = 1)
        #print(reg.shape)
        click.echo(reg.shape)

        #create Baseline Dataframe
        base = df.ix[df.ix[:,1] == 'Baseline Visit']
        base = base.drop(base.columns[2:30], axis = 1)
        base = base.drop(base.columns[23:37], axis = 1)
        base = base.drop(base.columns[417:651], axis = 1)
        #print(base.shape)
        click.echo(base.shape)

        #create Follow Up Dataframe
        fu = df[df.ix[:,1].str.contains('Follow-Up Visit')]
        fu = fu.drop(fu.columns[2:30], axis = 1)
        fu = fu.drop(fu.columns[9:23], axis = 1)
        fu = fu.drop(fu.columns[415:649], axis = 1)
        #print(fu.shape)
        click.echo(fu.shape)

        #create Surgery Dataframe
        surg = df.ix[df.ix[:,1] == 'Surgeries']
        surg = surg.drop(surg.columns[2:460], axis =1 )
        surg = surg.drop(surg.columns[194:235], axis = 1)
        #print(surg.shape)
        click.echo(surg.shape)

        #create Hospital Dataframe
        hosp = df.ix[df.ix[:,1] == 'Hospitalizations']
        hosp = hosp.drop(hosp.columns[2:652], axis = 1)
        #print(hosp.shape)
        click.echo(hosp.shape)

#print to csv
#reg.to_csv("reg.csv", sep =',')
#base.to_csv("base.csv", sep =',')
#fu.to_csv("fu.csv", sep =',')
#surg.to_csv("surg.csv", sep =',')
#hosp.to_csv("hosp.csv", sep =',')