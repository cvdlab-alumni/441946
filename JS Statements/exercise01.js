var i,j,string="";

for(i=1;i<=10;i++) {
	for(j=1;j<=10;j++) {
		string += i*j + "\t";
	}
	console.log(string);
	string = "";
}