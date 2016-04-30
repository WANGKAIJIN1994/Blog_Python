var checknumber = document.getElementById("form_comment").obtain.value;

var XMLHttp = {
    XMLHttpRequestPool:[],
    getInstance:function(){
        for(var i=0;i<this.XMLHttpRequestPool.length;i++){
            if(this.XMLHttpRequestPool[i].readyState==0 || this.XMLHttpRequestPool[i].readyState==4){
                return this.XMLHttpRequestPool[i];
            }
        }
        this.XMLHttpRequestPool[this.XMLHttpRequestPool.length] = this.createXMLHttpRequest();
        return this.XMLHttpRequestPool[this.XMLHttpRequestPool.length-1];
    },
    createXMLHttpRequest:function(){
        if(window.XMLHttpRequest){
            var objXMLHttp=new XMLHttpRequest();
        }
        else{
            var MSXML = ['MSXML2.XMLHttp.5.0','MSXML2.XMLHttp.4.0','MSXML2.XMLHttp.3.0',
            'MSXML2.XMLHttp','Microsoft.XMLHttp'];
            for(var n=0;n<MSXML.length;n++){
                try{
                    var objXMLHttp=new ActiveXObject(MSXML[n]);
                    break;
                }
                catch(e){}
            }
        }
        if(objXMLHttp.readyState==null){
            objXMLHttp.readyState=0;
            objXMLHttp.addEventListener("load",function(){
                objXMLHttp.readyState =4;
                if(typeof objXMLHttp.onreadystatechange == "function"){
                    objXMLHttp.onreadystatechange();
                }
            },false);
        }
        return objXMLHttp;
    },
    sendRequest:function(method,url,date,callback){
        var objXMLHttp = this.getInstance();
        with(objXMLHttp){
            try{
                if(url.indexOf("?")>0){
                    url += "&version="+Math.random();
                }
                else{
                    url += "?version="+Math.random();
                }
                open(method,url,true);
                if(method=="POST"){
                    setRequestHeader('Content-Type','application/x-www-form-urlencoded');
                    send(date);
                }
                if(method=="GET"){
                    send(null);
                }
                onreadystatechange = function(){
                    if(objXMLHttp.readyState == 4 && (objXMLHttp.status == 200||objXMLHttp.status==304)){
                        callback.call(null,objXMLHttp);
                    }
                }
            }
            catch(e){alert(e);}
        }
    }
};

function changenumber(objXMLHttp){
    checknumber = objXMLHttp.responseText;
    document.getElementById("form_comment").obtain.value = checknumber;
}

function obtaincheck(){
    XMLHttp.sendRequest("GET","/obtainnumber","",changenumber);
}

function showloginpage(){
    document.getElementById('display').style.display = 'block';
    document.getElementById('showloginpage').style.zIndex = 100;
    document.getElementById('showloginpage').style.display = 'block';
}

function closeloginpage(){
    document.getElementById('display').style.display = 'none';
    document.getElementById('showloginpage').style.zIndex = 0;
    document.getElementById('showloginpage').style.display = 'none';
}

function show_Login(){
    document.getElementById("setRegister").innerHTML = "";
    document.getElementById("form_login").action = "/login";
    document.getElementById("login").style.fontSize = "17px";
    document.getElementById("register").style.fontSize = "15px";
    document.getElementById("display").style.height = "230px";
    document.form_login.button.setAttribute("value","Sign In");
    document.form_login.button.setAttribute("onclich","login()");
}

function show_Register(){
    document.getElementById("setRegister").innerHTML = '<input onkeydown="switchline(event,form_login)" class="input all_radius" type="password" name="confirm" placeholder="confirm password:"/>';
    document.getElementById("register").style.fontSize = "17px";
    document.getElementById("login").style.fontSize = "15px";
    document.getElementById("form_login").action = "/register";
    document.getElementById("display").style.height = "270px";
    document.form_login.button.setAttribute("value","register");
    document.form_login.button.setAttribute("onclich","register()");
}

function switchline(event,formID){
    var keyCode = event.keyCode;
    if(keyCode == 13||keyCode == 39){
        var inputs = formID.getElementsByTagName('input');
        var input = document.getElementsByName(document.activeElement.name)[0];
        var count = 0;
        (function(){
                for(; count < inputs.length; count++){
                    if(input == inputs[count]){
                        count++;
                        break;
                }
            }
        })();
        inputs[count].focus();
        event.preventDefault();
    }
}

function check(formID){
    if(formID.comcontent != undefined && formID.comcontent.value == ""){
        alert("please enter the comments");
        return false;  
    }
    
    var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if(!reg.test(formID.email.value)){
        alert("please enter the right email");
        return false;
    }

    if(formID.password.value == ""){
        alert("please enter the password");
        return false;
    }

    if(formID.confirm != undefined){
        if(formID.confirm.value != formID.password.value){
            alert("The two passwords do not match");
            return false;
        }
    }

    if(formID.checknumber != undefined){
        if(formID.checknumber.value != checknumber){
            alert("the checknumber is wrong!");
            return false;
        }
    }
    return true;
}

function login(){
    if(check(form_login) == true){
        XMLHttp.sendRequest("POST","/login","wangkai",loginshow);
    }
    return false;
}

function loginshow(objXMLHttp){
    alert(objXMLHttp.responseText);
}

function register(){
    if(check(form_login) == true){
        XMLHttp.sendRequest("POST","/register", $("form_login").serialize(),registershow);
    }
    return false;
}


