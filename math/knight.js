function isSafe(x,y,n, board){
    return x>=0 && y >= 0 && x<n && y<n && board[x][y]=== -1;
}

function knightTourUtil(x,y,step,n,board, dx, dy){
    if (step === n*n){
        return true;
    }

    for(let i = 0; i<8; i++){
        let nx = x +dx[i]
        let ny= y+dy[i];

        if(isSafe(nx,ny,n,board)){
            board[nx][ny]= step;

            if (knightTourUtil(nx,ny,step+1,n, board, dx, dy)){
                return true;
            }

            board[nx][ny]= -1;
        }
    }
    return false;
}

function knightTour(n){
    let board = Array.from({length:n},()=> Array(n).fill(-1));

    let dx = [2,1,-1,-2,-2,-1,1,2];
    let dy = [1,2,2,1,-1,-2,-2,-1];

    board[0][0]= 0; 

    if(knightTourUtil(0,0,1,n,board,dx,dy)){
        return board;
    }

    return[[-1]];
}

    let n =5;
    let res = knightTour(n);
    for(let row of res){
        console.log(row.join(""));
    }
