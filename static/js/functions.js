function mtog(t) {
	target = document.getElementById('sm'+t);

	for (i=1;i<=10;i++) {
		oldtarget = document.getElementById('sm'+i);

		if (i !== t && oldtarget) {
			oldtarget.style.display='none';
			document.getElementById('m'+i).style.background='';
		} else if (i == t) {
			target.style.display='';
			document.getElementById('m'+i).style.background='#555';
		}
	}
}

function toggle ( target ) {
  if (document.getElementById) {
		target = document.getElementById( target );
			
		if (target.style.display == "none") {
			target.style.display 	= "";
		} else {
			target.style.display 	= "none";
		}
	}
}

function togglep (target,word,wordon,wordoff) {
	if (document.getElementById) {
		target 	= document.getElementById(target);
		word	= document.getElementById(word);

		if (target.style.display == "none") {
			target.style.display 	= "";
			word.innerHTML			= wordoff;
		}
		else {
			target.style.display 	= "none";
			word.innerHTML			= wordon;
		}
	}
}

function SetSelectByValue(sel,val){for (var i=0,opts=sel.options,len=opts.length;i<len;i++) {if (opts[i].value==val) {return sel.selectedIndex=i;}}}

function checkEmail(email) {
	if (email.match(/\b(^(\S+@).+((\.com)|(\.net)|(\.edu)|(\.mil)|(\.gov)|(\.org)|(\..{2,2}))$)\b/gi) == false) {alert("invalid email");return false;}
	else {return true;}
}

function yousure(msg) {
	if (!msg) {msg = "Are you sure?";}
	var where_to= confirm(msg);
	if (where_to == true) {return true;} else if (where_to == false) {return false;}
}

function LTrim(str) {
	var whitespace = new String(" \t\n\r");
	var s = new String(str);

	if (whitespace.indexOf(s.charAt(0)) != -1) {
		var j=0, i = s.length;
		while (j < i && whitespace.indexOf(s.charAt(j)) != -1) {j++;s = s.substring(j, i);}
	}
	return s;
}

function RTrim(str) {
	var whitespace = new String(" \t\n\r");
	var s = new String(str);

	if (whitespace.indexOf(s.charAt(s.length-1)) != -1) {
		var i = s.length - 1;       // Get length of string
		while (i >= 0 && whitespace.indexOf(s.charAt(i)) != -1) {i--;s = s.substring(0, i+1);}
	}
	return s;
}
	
function trim(str) {return RTrim(LTrim(str));}