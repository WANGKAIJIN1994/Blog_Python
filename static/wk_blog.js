var checknumber;

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
    sendRequest:function(method,url,date){
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
                        checknumber = objXMLHttp.responseText;
                    }
                }
            }
            catch(e){alert(e);}
        }
    }
};

function obtaincheck(){
        XMLHttp.sendRequest("GET","obtaincheck","")
}


function check(){
    if(form_comment.comcontent.value ==""){
        alert("please enter the comments");
        return false;  
    }
    
    var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if(!reg.test(form_comment.email.value)){
        alert("please enter the right email");
        return false;
    }

    if(form_comment.password.value == ""){
        alert("please enter the password");
        return false;
    }

    if(form_comment.checknumber.value != checknumber){
        alert("the checknumber is wrong!");
        return false;
    }
}

function switchline(event){
    var keyCode = event.keyCode;
    if(keyCode == 13||keyCode == 39){
        var inputs = document.getElementById('form_comment').getElementsByTagName('input');
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

