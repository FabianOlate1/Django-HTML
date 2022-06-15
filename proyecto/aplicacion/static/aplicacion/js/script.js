const mapdiv = document.getElementById("map");
let map
function initmap() {
  map = new google.maps.Map(mapdiv,{
    center: {lat:-34.5956145 ,lng: -58.4431949},
    zoom : 8
  })
}

