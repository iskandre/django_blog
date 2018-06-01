from django.shortcuts import render
from django.http import HttpResponse
import pickle
import os

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def index(request):
    return render(request,'home/index.htm')

def intro_post(request):
    return render(request,'home/introduction_post.htm', {'loop':'/media/iskandre/loop.png','loop1':'/media/iskandre/loop1.png'})

def abtest_post(request):
    return render(request,'home/ab_test_post.htm')

# Create your views here.
def post(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    resDict_iskandre = {}
    resDict_path = '/root/website/instagram_tool_project/cached_data/iskandre/resultDict.txt'
    resDict_path = dir_path + '/cached_data/iskandre/resultDict.txt'
    if os.path.isfile(resDict_path) == True:
        with open(resDict_path, 'rb') as f:           
            while 1:
                try:
                    resDict_iskandre.update(pickle.load(f))
                except EOFError:
                    break
                
    resDict_natalie = {}
    resDict_path = '/root/website/instagram_tool_project/cached_data/natalie_sn0w/resultDict.txt'
    resDict_path = dir_path + '/cached_data/iskandre/resultDict.txt'
    if os.path.isfile(resDict_path) == True:
        with open(resDict_path, 'rb') as f:
            while 1:
                try:
                    resDict_natalie.update(pickle.load(f))
                except EOFError:
                    break
    
    temp_dict = {}   
    for item in resDict_natalie['root_users_dict'].keys():
        temp_dict[item] = resDict_natalie['root_users_dict'][item]
        if len(temp_dict) > 7:
            break
        
    print('resDict_natalie keys %s' %resDict_natalie.keys())

#    temp_dict = resDict_natalie['root_users_dict']
#    resDict_iskandre_natalie['root_users_dict'] = take(10, temp_dict.items())
    resDict_iskandre['correlation_heatmap_graph'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['correlation_heatmap_graph'].split('/')[len(resDict_iskandre['correlation_heatmap_graph'].split('/')) - 1]
    print('correlation_heatmap_graph updated %s' %resDict_iskandre['correlation_heatmap_graph'])
    resDict_iskandre['pairplot_homeCountry_graph'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_homeCountry_graph'].split('/')[len(resDict_iskandre['pairplot_homeCountry_graph'].split('/')) - 1]
    resDict_iskandre['pairplot_main_graph'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_main_graph'].split('/')[len(resDict_iskandre['pairplot_main_graph'].split('/')) - 1]
    resDict_iskandre['pairplot_followed_by'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_followed_by'].split('/')[len(resDict_iskandre['pairplot_followed_by'].split('/')) - 1]
    resDict_iskandre['pairplot_follows'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_follows'].split('/')[len(resDict_iskandre['pairplot_follows'].split('/')) - 1]
    resDict_iskandre['pairplot_posts_count'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_posts_count'].split('/')[len(resDict_iskandre['pairplot_posts_count'].split('/')) - 1]
    resDict_iskandre['pairplot_countriesCount'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_countriesCount'].split('/')[len(resDict_iskandre['pairplot_countriesCount'].split('/')) - 1]
    resDict_iskandre['pairplot_avgPostingFreq'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_avgPostingFreq'].split('/')[len(resDict_iskandre['pairplot_avgPostingFreq'].split('/')) - 1]
    resDict_iskandre['pairplot_withGeo'] = '/media/' + 'iskandre' + '/' + resDict_iskandre['pairplot_withGeo'].split('/')[len(resDict_iskandre['pairplot_withGeo'].split('/')) - 1]
                
    return render(request,'home/analysis_post.htm',{'followerCTR_map':resDict_iskandre['followerCTR_map'],'sum_followers_map':resDict_iskandre['sum_followers_map'],
                                                 'results_table':temp_dict,'clusters_string':resDict_natalie['stringJson'],
                                                 'clusters_table':resDict_natalie['resDf'],
                                                 'correlation_heatmap_graph': resDict_iskandre['correlation_heatmap_graph'],
                                    'pairplot_homeCountry_graph':resDict_iskandre['pairplot_homeCountry_graph'],
                                    'pairplot_main_graph':resDict_iskandre['pairplot_main_graph'],
                                    'pairplot_followed_by':resDict_iskandre['pairplot_followed_by'],
                                    'pairplot_follows':resDict_iskandre['pairplot_follows'],'pairplot_posts_count':resDict_iskandre['pairplot_posts_count'],
                                    'pairplot_countriesCount':resDict_iskandre['pairplot_countriesCount'],'pairplot_avgPostingFreq':resDict_iskandre['pairplot_avgPostingFreq'],
                                    'df_userMapScreen':'/media/iskandre/dfUserMap_example.png',
                                    'bugsModelScreen':'/media/iskandre/bugs_model_screenshot.png',
                                    'pairplot_withGeo':resDict_iskandre['pairplot_withGeo'],
                                    'b1':'/media/iskandre/b1.png','b2':'/media/iskandre/b2.png',
                                    'b3':'/media/iskandre/b3.png','b4':'/media/iskandre/b4.png',
                                    'b5':'/media/iskandre/b5.png','b6':'/media/iskandre/b6.png',
                                    'b7':'/media/iskandre/b7.png','b8':'/media/iskandre/b8.png',
                                    'b9':'/media/iskandre/b9.png','b10':'/media/iskandre/b10.png'
                                                 })


def blog(request):
    return HttpResponse("Blog is coming soon")