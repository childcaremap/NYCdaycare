 clear
 [~,~,known]=xlsread('29mar2014_geocoded.csv');
 
 [~,~,new]=xlsread('04apr2014_combined.csv');
 
 %find columns
 iname = find(ismember(known(1,:),'Center Name'));
 iholder = find(ismember(known(1,:),'Permit Holder'));
 iaddress = find(ismember(known(1,:),'Address'));
 izip= find(ismember(known(1,:),'Zip Code'));
 iphone = find(ismember(known(1,:),'Phone'));
 ipermit = find(ismember(known(1,:),'Permit Number'));
 iexp = find(ismember(known(1,:),'Permit Expiration Date'));
 istatus = find(ismember(known(1,:),'Permit Status'));
 iagerange= find(ismember(known(1,:),'Age Range'));
 icap = find(ismember(known(1,:),'Maximum Capacity'));
 imed = find(ismember(known(1,:),'Certified To Administer Medication'));
 itype = find(ismember(known(1,:),'Site Type'));
 ilon = find(ismember(known(1,:),'Lon'));
 ilat = find(ismember(known(1,:),'Lat'));
 
 %make zip codes into strings
 known(2:end,izip) = cellfun(@num2str,known(2:end,izip),'UniformOutput',false);
 new(2:end,izip) = cellfun(@num2str,new(2:end,izip),'UniformOutput',false);
%  %make lat and lon into strings, easier to handle cell arrays of strings
%  known(2:end,ilon) = cellfun(@num2str,known(2:end,ilon),'UniformOutput',false);
%  known(2:end,ilat) = cellfun(@num2str,known(2:end,ilat),'UniformOutput',false);
 
 %combdata = known(1,:);
 %k = 2;
 for i = 2: length(new)
     if ~isempty(find(ismember(known(:,iaddress),cell2mat(new(i,iaddress)))&ismember(known(:,izip),cell2mat(new(i,izip)))))
        i_found = find(ismember(known(:,iaddress),cell2mat(new(i,iaddress)))&ismember(known(:,izip),cell2mat(new(i,izip))));
        new(i,ilon) = known(i_found(1),ilon);
        new(i,ilat) = known(i_found(1),ilat);
     else
        
     end
 end
 
 xlswrite('04apr2014_combined_geocoded.xls',new);
