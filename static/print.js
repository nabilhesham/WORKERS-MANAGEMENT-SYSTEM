window.onload=function(){
  console.log("loaded!!!")
  window.print()
  window.onafterprint = function(){
    window.location.href = "http://127.0.0.1:8000/workers/";
  }
}
