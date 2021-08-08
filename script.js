var num = 1;

function newlocation(){
  
  num += 1;

  if (num >= 11){
    alert("You have reached the maximum number of locations");
    return;
  }

  var name = "location" + num.toString();

  console.log(name);

  var location = document.createElement("INPUT");
  location.setAttribute("type", "text");
  location.setAttribute("id", "autocomplete");
  location.setAttribute("name", name);
  location.setAttribute("class", "form-control");
  location.setAttribute("placeholder", "Location");
  

  document.getElementById("locationform").appendChild(location);   
}