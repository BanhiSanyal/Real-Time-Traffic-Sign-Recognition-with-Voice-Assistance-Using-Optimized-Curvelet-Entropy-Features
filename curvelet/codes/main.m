%% Curvelet Features for images classification 
% all level coefficients are used for feature extraction
clc;
close all;
clear all;
%% Input image
a=imread('cameraman.tif');
[r,c]=size(a);

featureVector=feature_vector_curvelet(a); %% For more number of images use a "For" loop
finalFeatureVector=abs(featureVector);
%global k;
%k=input('Enter the number of largest coefficients U want to take: ');
%featureMatrix;

