function [f] = feature_vector_curvelet( iname )
a=iname;
%disp('Take curvelet transform: fdct_wrapping');
C = fdct_wrapping(a,0);
m=size(C,2); % no of level
f=[];
%global k;
for i=1:m
    n=size(C{1,i},2); % no of subbands in each level
    n1=ceil(n/2);  % Symmetric subbands are discarded
    for j=1:n1
        [x,y]=size(C{i}{j});
        coeff=reshape((C{i}{j})',1,x*y);
        %sort_coeff=sort(coeff,'descend');
        %k=input('Enter the number of largest coefficients U want to take: ');
        %largest_coeff=sort_coeff(1:k);
        if isempty(f)
            f=coeff;
        else
        f=[f, coeff];
        end
    end
end
f;
end

