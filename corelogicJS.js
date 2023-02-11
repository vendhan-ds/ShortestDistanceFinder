console.log("hi")
let v=5

/* var canvas=document.querySelector('canvas')
canvas.width=window.innerWidth-25;
canvas.height=700;
var c=canvas.getContext("2d"); 
c.beginPath(); */

let mat=[[0,3,0,0,4],[3,0,2,0,5],[0,2,0,6,1],[0,0,6,0,0],[4,5,1,0,0]]

function printPathUtil(u,d,visited,path,pi,count){
    //console.log("entered util")
    visited[u]=1;
    path[pi]=u;
    pi++

    if(u==d){
        //feeder(path,count);
        console.log("path length:", count)
        for(let j=0;j<pi;j++){
            console.log(path[j])
        } 
    }else{
        let temp=mat[u]
        //console.log("temp:",temp,"path",path)
        for(let k=0;k<v;k++){
            let temp2=temp[k]
            if(temp2!=0 && visited[k]==0){
                count=count+temp2
                printPathUtil(k,d,visited,path,pi,count)
                count=count-temp2
            }
        }
    }
    pi--
    visited[u]=0
}

function printPath(s,d){
    //console.log("entered driver")
    count=0
    let visited=[]
    let path=[]
    let pi=0
    for(let i=0;i<v;i++){
        visited[i]=0
    }
    printPathUtil(s,d,visited,path,pi,count)

}  

printPath(0,3)