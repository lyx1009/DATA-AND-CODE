// import Excel
import excel "D:\7月21数据\Flat\London_flat.xlsx", sheet("Sheet1") firstrow clear
// replace by "terrace","detached" subsequently

// drop missing values
drop if missing(price,size,beds,baths,neareststations,region,density,builthouses,weeklysalary,unemploymentrate,crimes)

// deal with outlier
winsor2 price size, cut (1 99) replace

// descriptive analysis
tabstat price size beds baths neareststations density builthouses weeklysalary unemploymentrate crimes, s(N mean sd min max) f(%12.3f) c(s)

// correlation
pwcorr_a price size beds baths neareststations density builthouses weeklysalary unemploymentrate crimes

// standardize
egen price_z = std(price)
egen size_z = std(size)
egen beds_z = std(beds)
egen baths_z = std(baths)
egen neareststations_z = std(neareststations)
egen density_z = std(density)
egen builthouses_z = std(builthouses)
egen weeklysalary_z = std(weeklysalary)
egen unemploymentrate_z = std(unemploymentrate)
egen crimes_z = std(crimes)

// regression (ols) by group 
bysort region: reg price_z neareststations_z weeklysalary_z crimes_z size_z beds_z baths_z density_z builthouses_z unemploymentrate_z

// hypothesis testing
ssc install bdiff

// Permutation
gen location = 0
replace location = 1 if region == "Inner London"
// testing 
bdiff, group(location) model(reg price_z neareststations_z weeklysalary_z crimes_z size_z beds_z baths_z density_z builthouses_z unemploymentrate_z)reps(100) 

