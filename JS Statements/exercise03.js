var i,j,string="";

for(i=1;i<=10;i++) {
	for(j=1;j<=9;j++) {
		if(j===i)
			string += 1 + ",\t";
		else
			string += 0 + ",\t";
	}
	if(j===i)
			string += 1 + "\t";
		else
			string += 0 + "\t";
	console.log(string);
	string = "";
}