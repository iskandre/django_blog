from django.shortcuts import render
from django.http import HttpResponse
from tool.forms import showStatisticsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


import re
import requests
import numpy as np
import pandas as pd
import logging as log
from abc import ABCMeta, abstractmethod
import time
import pickle
import random
import inspect, os, pathlib
from os.path import basename
from itertools import islice
import sys  

import json
import bs4
from itertools import groupby
from collections import Counter
import collections
from collections import OrderedDict
#from langdetect import detect_langs
import math
from langdetect import detect_langs
from langdetect import detect
import nltk
from nltk.tag.stanford import StanfordNERTagger
from stop_words import get_stop_words
import os

#sys.setdefaultencoding('utf8')
#sys.path.append(os.getcwd())
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import CountVectorizer
from pyspark import SparkFiles
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import unicodedata
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg import SparseVector, DenseVector

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
# $example on$
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.sql import SQLContext

#from pyspark.mllib.feature import IDF

from pyspark.ml.linalg import Vectors
from pyspark.ml.clustering import LDA,LDAModel
from pyspark.ml.linalg import Vectors, SparseVector
from operator import itemgetter

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def calculation(infoType,account,test):
    analysisFile_path = account.link_to_files
    analysisFile_path1 = account.link_to_files1
    print('analysisFile_path1 %s' %analysisFile_path1)
    
    if infoType == 'basic':  
        if account.name == 'iskandre':
            return {}
            resDict = {}
            if os.path.isfile(account.resDict_path) == True:
                with open(account.resDict_path, 'rb') as f:           
                    while 1:
                        try:
                            resDict.update(pickle.load(f))
                        except EOFError:
                            break
            return resDict['root_users_dict']
            
        myFollowers_tracking = {}
        #    analysisFile_path = '/Users/iskandre/Documents/instagram_python/girls/analysis'
        #    analysisFile_path1 = '/Users/iskandre/Documents/instagram_python/girls/analysis'
        with open('%s/followed_users_tracking.txt' % analysisFile_path1, 'rb') as f:           
            while 1:
                try:
                    myFollowers_tracking.update(pickle.load(f))
                except EOFError:
                    break
        
            likers = {}
            followers = []
            unfollowers = []
            myFollowers = {}
            with open('%s/followed_users_tracking.txt' % analysisFile_path1, 'rb') as f:           
                while 1:
                    try:
                        myFollowers.update(pickle.load(f))
                    except EOFError:
                        break
                    
            analytics_followed_userids = []
            with open('%s/analytics_followed_userids.txt' % analysisFile_path, 'rb') as f:           
                while 1:
                    try:
                        analytics_followed_userids.append(pickle.load(f))
                    except EOFError:
                        break
            
            for k,v in myFollowers.items():
                if 'liked_posts' in v.keys():
                    likes_count = len(v['liked_posts'])
                    likers.update({k:likes_count})
                if 'follow' in v.keys():
                    followers.append(k)
                if 'unfollow' in v.keys():
                    unfollowers.append(k)
                    
            print('len  unfollow%s' %len(unfollowers))
            print('len followers %s' %len(followers))
            print('len likers %s' %len(likers))
            print('len analytics_followed_userids %s' %len(analytics_followed_userids))
                    
            people_who_followed = {}
            for k,v in myFollowers_tracking.items():
                if 'follow' in v.keys():
                    people_who_followed[k] = v
            people_who_followed = OrderedDict(sorted(people_who_followed.items(), key=lambda kv: kv[1]['follow']))
        
            # statistics about root bloggers
            root_users_dict = {}
            
            for item in analytics_followed_userids:
                root_user = list(item.values())[0]['root_username']
                user = list(item.keys())[0]
                if root_user in root_users_dict.keys():
                    print('if true')
                    current_records_number = root_users_dict[root_user]['records']
                    root_users_dict[root_user].update({'records':(current_records_number+1)})
                    if user in followers:                    
                        # check at home: follower keyword must be in the array element
                        item[user].update({'follower':True})
                        if 'follow' in root_users_dict[root_user].keys():
                            current_follow_number = root_users_dict[root_user]['follow']
                            root_users_dict[root_user].update({'follow':(current_follow_number + 1)})
                        else:
                            root_users_dict[root_user].update({'follow':1})
                    if user in likers:
                        if 'like' in root_users_dict[root_user].keys():
                            current_follow_number = root_users_dict[root_user]['like']
                            root_users_dict[root_user].update({'like':(current_follow_number + 1)})
                        else:
                            root_users_dict[root_user].update({'like':1})
                    if user in unfollowers:
                        if 'unfollow' in root_users_dict[root_user].keys():
                            current_follow_number = root_users_dict[root_user]['unfollow']
                            root_users_dict[root_user].update({'unfollow':(current_follow_number + 1)})
                        else:
                            root_users_dict[root_user].update({'unfollow':1})
                else:
                    root_users_dict.update({root_user:{'records':1}})
                    if user in followers:
                        root_users_dict[root_user].update({'follow':1})
                    if user in likers:
                        root_users_dict[root_user].update({'like':1})
                    if user in unfollowers:
                        root_users_dict[root_user].update({'unfollow':1})

            return root_users_dict
        
    elif infoType == 'clusters':
        resDict = {}
        if os.path.isfile(account.resDict_path) == True:
            with open(account.resDict_path, 'rb') as f:           
                while 1:
                    try:
                        resDict.update(pickle.load(f))
                    except EOFError:
                        break
        
        return (resDict['stringJson'],resDict['resDf'],resDict['best_hashtags'],resDict['worst_hashtags'])
    elif infoType == 'geography':
        resDict = {}
        if os.path.isfile(account.resDict_path) == True:
            with open(account.resDict_path, 'rb') as f:
                while 1:
                    try:
                        resDict.update(pickle.load(f))
                    except EOFError:
                        break
        return (resDict['followerCTR_map'],resDict['likerCTR_map'],resDict['sum_followers_map'])
    elif infoType == 'analysis':
        resDict = {}
        if os.path.isfile(account.resDict_path) == True:
            with open(account.resDict_path, 'rb') as f:           
                while 1:
                    try:
                        resDict.update(pickle.load(f))
                    except EOFError:
                        break
        print('correlation_heatmap_graph %s' %resDict['correlation_heatmap_graph'])
        resDict['correlation_heatmap_graph'] = '/cached_data/' + account.name + '/' + resDict['correlation_heatmap_graph'].split('/')[len(resDict['correlation_heatmap_graph'].split('/')) - 1]
        print('correlation_heatmap_graph updated %s' %resDict['correlation_heatmap_graph'])
        resDict['pairplot_homeCountry_graph'] = '/cached_data/' + account.name + '/' + resDict['pairplot_homeCountry_graph'].split('/')[len(resDict['pairplot_homeCountry_graph'].split('/')) - 1]
        resDict['pairplot_main_graph'] = '/cached_data/' + account.name + '/' + resDict['pairplot_main_graph'].split('/')[len(resDict['pairplot_main_graph'].split('/')) - 1]
        resDict['pairplot_followed_by'] = '/cached_data/' + account.name + '/' + resDict['pairplot_followed_by'].split('/')[len(resDict['pairplot_followed_by'].split('/')) - 1]
        resDict['pairplot_follows'] = '/cached_data/' + account.name + '/' + resDict['pairplot_follows'].split('/')[len(resDict['pairplot_follows'].split('/')) - 1]
        resDict['pairplot_posts_count'] = '/cached_data/' + account.name + '/' + resDict['pairplot_posts_count'].split('/')[len(resDict['pairplot_posts_count'].split('/')) - 1]
        resDict['pairplot_countriesCount'] = '/cached_data/' + account.name + '/' + resDict['pairplot_countriesCount'].split('/')[len(resDict['pairplot_countriesCount'].split('/')) - 1]
        resDict['pairplot_avgPostingFreq'] = '/cached_data/' + account.name + '/' + resDict['pairplot_avgPostingFreq'].split('/')[len(resDict['pairplot_avgPostingFreq'].split('/')) - 1]
        return (resDict['correlation_heatmap_graph'],resDict['pairplot_homeCountry_graph'],resDict['pairplot_main_graph'],
                resDict['pairplot_followed_by'],resDict['pairplot_follows'],resDict['pairplot_posts_count'],
                resDict['pairplot_countriesCount'],resDict['pairplot_avgPostingFreq'])
    elif infoType == 'advanced':
        return ''
            

def statistics(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = showStatisticsForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            data = form.cleaned_data
            results = calculation(data['informationType'],data['account'],data['test'])
            print('data = %s' %data)
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # redirect to a new URL:
            if data['informationType'] == 'basic':
                return render(request,'tool/results.html',{'results':results, 'form':form})
            elif data['informationType'] == 'clusters':
                return render(request,'tool/results_clusters.html',{'stringJson': results[0],
                                                                    'resDf':results[1],
                                                                    'best_hashtags':results[2],
                                                                    'worst_hashtags':results[3], 'form':form})
            elif data['informationType'] == 'geography':
                return render(request,'tool/results_geography.html',{'followerCTR_map': results[0],
                                                    'likerCTR_map':results[1],
                                                    'sum_followers_map':results[2],'form':form})
            elif data['informationType'] == 'analysis':
                return render(request,'tool/results_analysis.html',{'correlation_heatmap_graph': results[0],
                                    'pairplot_homeCountry_graph':results[1],
                                    'pairplot_main_graph':results[2],'pairplot_followed_by':results[3],
                                    'pairplot_follows':results[4],'pairplot_posts_count':results[5],
                                    'pairplot_countriesCount':results[6],'pairplot_avgPostingFreq':results[7],'form':form})
            elif data['informationType'] == 'advanced':
                return render(request,'tool/results_advanced.html',{'form':form})
                
#            return HttpResponseRedirect(reverse('/') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = showStatisticsForm(initial={})

    return render(request, 'tool/statistics.html', {'form': form})