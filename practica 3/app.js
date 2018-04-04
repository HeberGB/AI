'esversion: 6';

function shuffle(array) {
    var currentIndex = array.length,
        temporaryValue, randomIndex;

    while (0 !== currentIndex) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function fillBoard() {
    let parts = ['00', '01', '02', '03', '10', '11', '12', '13', '20', '21', '22', '23', '30', '31', '32', 'Empty'];
    let matrix = [];
    let empty = 0;
    for (let i = 0; i < 4; i++) {
        let temp = new Array(4);
        for (let j = 0; j < 4; j++) {
            parts = shuffle(parts);
            temp[j] = parts.pop();
            if (temp[j] === 'Empty') {
                empty = {
                    x: j,
                    y: i
                };
            }
            document.getElementById(i.toString() + j.toString()).innerHTML = temp[j] === 'Empty' ? '' : '<img src="img/' + temp[j] + '.jpg">';
        }
        matrix.push(temp);
    }
    let board = new Board(matrix, empty);
    return board;
}

class Board {
    constructor(matrix, empty) {
        this.matrix = matrix;
        this.empty = empty;
    }
    order() {
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if (this.matrix[i][j] === i.toString() + j.toString()) {
                    console.log(this.matrix[i][j]);
                    
                    continue;
                } else {
                    return false;
                }

            }
        }
        return false;
    }
    rigthMove() {
        let aux = this.matrix;
        let emptyAux = this.empty;
        aux[emptyAux.y][emptyAux.x] = aux[emptyAux.y][emptyAux.x + 1];
        aux[emptyAux.y][emptyAux.x + 1] = 'Empty';
        this.empty = {
            x: emptyAux.x + 1,
            y: emptyAux.y
        }
        return new Board(aux, emptyAux);

    }
    leftMove() {
        let aux = this.matrix;
        let emptyAux = this.empty;
        aux[emptyAux.y][emptyAux.x] = aux[emptyAux.y][emptyAux.x - 1];
        aux[emptyAux.y][emptyAux.x - 1] = 'Empty';
        this.empty = {
            x: emptyAux.x - 1,
            y: emptyAux.y
        }
        return new Board(aux, emptyAux);
    }
    upMove() {
        let aux = this.matrix;
        let emptyAux = this.empty;
        aux[emptyAux.y][emptyAux.x] = aux[emptyAux.y - 1][emptyAux.x];
        aux[emptyAux.y - 1][emptyAux.x] = 'Empty';
        this.empty = {
            x: emptyAux.x,
            y: emptyAux.y - 1
        }
        return new Board(aux, emptyAux);
    }
    downMove() {
        let aux = this.matrix;
        let emptyAux = this.empty;
        aux[emptyAux.y][emptyAux.x] = aux[emptyAux.y + 1][emptyAux.x];
        aux[emptyAux.y + 1][emptyAux.x] = 'Empty';
        this.empty = {
            x: emptyAux.x,
            y: emptyAux.y + 1
        }
        return new Board(aux, emptyAux);
    }
}

class Node {
    constructor(board) {
        this.board = board;
        if (this.board.empty.x === 3) {
            return;
        } else if (this.board.empty.x === 0) {
            this.left = null;
            if (this.board.empty.y === 0) {
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = null;
            } else if (this.board.empty.y === 3) {
                this.rigth = new Node(this.board.rigthMove());
                this.down = null;
                this.up = new Node(this.board.upMove());
            } else {
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = new Node(this.board.upMove());
            }

        } else if (this.board.empty.x === 3) {
            this.rigth = null;
            if (this.board.empty.y === 0) {
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = null;
            } else if (this.board.empty.y === 3) {
                this.rigth = new Node(this.board.rigthMove());
                this.down = null;
                this.up = new Node(this.board.upMove());
            } else {
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = new Node(this.board.upMove());
            }

        } else {
            if (this.board.empty.y === 0) {
                this.left = new Node(this.board.leftMove());
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = null;
            } else if (this.board.empty.y === 3) {
                this.left = new Node(this.board.leftMove());
                this.rigth = new Node(this.board.rigthMove());
                this.down = null;
                this.up = new Node(this.board.upMove());
            } else {
                this.left = new Node(this.board.leftMove());
                this.rigth = new Node(this.board.rigthMove());
                this.down = new Node(this.board.downMove());
                this.up = new Node(this.board.upMove());
            }
        }
    }
}

class treeSolution {
    constructor(board) {
        this.node = null;
    }
}

let board = fillBoard();
let tree = new Node(board);
console.log(board);

function findTheAnswer(board) {

}