function calcola(bytes) {
  packets=Math.ceil(bytes/(576-(20+8)));
  var risp=bytes+" bytes sono incapsulati in "+packets+" pacchetti"
  document.getElementById("domanda").innerHTML = risp
}
