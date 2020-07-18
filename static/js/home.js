
function verify_input(){
    let content = document.getElementById("url_input").value
    if (content == ""){
        document.getElementById("warningtext").innerHTML = "URL field cannot be empty"
        return false
    }
    else{
        document.getElementById("warningtext").innerHTML = ""
    }
    return true
}