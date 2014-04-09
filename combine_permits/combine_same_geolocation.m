 clear
 [~,~,raw]=xlsread('04apr2014_combined_geocoded.csv');
 
 %find columns
 iname = find(ismember(raw(1,:),'Center Name'));
 iholder = find(ismember(raw(1,:),'Permit Holder'));
 iaddress = find(ismember(raw(1,:),'Address'));
 izip= find(ismember(raw(1,:),'Zip Code'));
 iphone = find(ismember(raw(1,:),'Phone'));
 ipermit = find(ismember(raw(1,:),'Permit Number'));
 iexp = find(ismember(raw(1,:),'Permit Expiration Date'));
 istatus = find(ismember(raw(1,:),'Permit Status'));
 iagerange= find(ismember(raw(1,:),'Age Range'));
 icap = find(ismember(raw(1,:),'Maximum Capacity'));
 imed = find(ismember(raw(1,:),'Certified To Administer Medication'));
 itype = find(ismember(raw(1,:),'Site Type'));
 ilon = find(ismember(raw(1,:),'Lon'));
 ilat = find(ismember(raw(1,:),'Lat'));
 
 %make zip codes into strings
 raw(2:end,izip) = cellfun(@num2str,raw(2:end,izip),'UniformOutput',false);
 %make lat and lon into strings, easier to handle cell arrays of strings
 raw(2:end,ilon) = cellfun(@num2str,raw(2:end,ilon),'UniformOutput',false);
 raw(2:end,ilat) = cellfun(@num2str,raw(2:end,ilat),'UniformOutput',false);
 
 combdata = raw(1,:);
 k = 2;
 for i = 2: length(raw)
     if isempty(find(ismember(combdata(:,ilat),cell2mat(raw(i,ilat)))&ismember(combdata(:,ilon),cell2mat(raw(i,ilon)))))
        %isempty(find(ismember(combdata(:,iaddress),cell2mat(raw(i,iaddress)))&ismember(combdata(:,izip),cell2mat(raw(i,izip)))))
        %add entry if lat long is not the same as any other entry
        combdata(k,:) = raw(i,:);
%         %adjust format of expiration date
%         expdate = cell2mat(raw(i,iexp));
%         expdatenum = num2str(expdate/10^11);
%         year = expdatenum(1:4);
%         month = expdatenum(5:6);
%         combdata(k,iexp) = {[year,'-',month]};
        %make permit number a string
        combdata(k,ipermit) = {num2str(cell2mat(combdata(k,ipermit)))};
        k = k+1;
     else
        %locate other entry with same lat, lon
        i_comb = find(ismember(combdata(:,ilat),cell2mat(raw(i,ilat)))&ismember(combdata(:,ilon),cell2mat(raw(i,ilon))));
        %locate other entry with same address
        %problem is with closeby addresses but same lat lon
        %i_comb = find(ismember(combdata(:,iaddress),cell2mat(raw(i,iaddress)))&ismember(combdata(:,izip),cell2mat(raw(i,izip))));
        %combine age ranges of two permits
        combagerange = [raw(i,iagerange),combdata(i_comb,iagerange)];
        minage = min([str2num(combagerange{1}(1)),str2num(combagerange{2}(1))]);
        maxage = max([str2num(combagerange{1}(11)),str2num(combagerange{2}(11))]);
        combstr = cell2mat(combdata(i_comb,iagerange));
        combstr(1) = num2str(minage);
        combstr(11) = num2str(maxage);
        combdata(i_comb,iagerange) = {combstr};
        combdata(i_comb,icap) = {cell2mat(combdata(i_comb,icap))+cell2mat(raw(i,icap))};
%         %adjust format of expiration date
%         expdate = cell2mat(raw(i,iexp));
%         expdatenum = num2str(expdate/10^11);
%         year = expdatenum(1:4);
%         month = expdatenum(5:6);
        %combine expiration dates of both premits
        combdata(i_comb,iexp) = {[cell2mat(combdata(i_comb,iexp)),' / ',cell2mat(raw(i,iexp))]};
        %combine permit statuses of both permits
        combdata(i_comb,istatus) = {[cell2mat(combdata(i_comb,istatus)),' / ',cell2mat(raw(i,istatus))]};
        %combine permit number of both permits
        combdata(i_comb,ipermit) = {[num2str(cell2mat(combdata(i_comb,ipermit))),' / ',num2str(cell2mat(raw(i,ipermit)))]};
        if ~strcmp(combdata(i_comb,iname),raw(i,iname))
            %combine center names if not the same
            combdata(i_comb,iname) = {[cell2mat(combdata(i_comb,iname)),' / ',cell2mat(raw(i,iname))]};
        end
        if ~strcmp(combdata(i_comb,iholder),raw(i,iholder))
            %combine permit holders if not the same
            combdata(i_comb,iholder) = {[cell2mat(combdata(i_comb,iholder)),' / ',cell2mat(raw(i,iholder))]};
        end
        if ~strcmp(combdata(i_comb,iphone),raw(i,iphone))
            %combine phone number if not the same
            combdata(i_comb,iphone) = {[cell2mat(combdata(i_comb,iphone)),' / ',cell2mat(raw(i,iphone))]};
        end
        if ~strcmp(combdata(i_comb,iaddress),raw(i,iaddress))
            %combine address if not the same (despite same geolocation)
            combdata(i_comb,iaddress) = {[cell2mat(combdata(i_comb,iaddress)),' / ',cell2mat(raw(i,iaddress))]};
        end
        if ~strcmp(combdata(i_comb,itype),raw(i,itype))
            %combine permit types if not the same
            combdata(i_comb,itype) = {[cell2mat(combdata(i_comb,itype)),' / ',cell2mat(raw(i,itype))]};
        end
        if ~strcmp(combdata(i_comb,imed),raw(i,imed))
            %combine medication permit if not the same
            combdata(i_comb,imed) = {[cell2mat(combdata(i_comb,imed)),' / ',cell2mat(raw(i,imed))]};
        end
     end
 end
 
 xlswrite('04apr2014_combined_geocoded.xls',combdata);
