// var contDeReflejos =0;

// const cajaDeNums = [2,3,2,5,4,5,3,5]//23254535.3547634534
// tamArray = cajaDeNums.length;
// console.log('tiene tam de: '+tamArray);
function tieneReflejo(){//contDeReflejos, cajaDeNums){
    var contDeReflejos = 0; const cajaDeNums = [2,3,2,5,4,5,3,5]//23254535.3547634534
    for (i= 1; i <= cajaDeNums.length - 2;i++ ){
        if(cajaDeNums[i-1] == cajaDeNums[i+1]){
            contDeReflejos++;console.log(contDeReflejos)}}
    console.log(contDeReflejos+' Tienen reflejos');}
tieneReflejo();