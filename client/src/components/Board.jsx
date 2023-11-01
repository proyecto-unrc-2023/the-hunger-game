import React from "react";
import "./Board.css";
import Cell from './Cell';

const Board = ({ size, boardState}) => {
  const extraCells = 3;
  const extra = extraCells * 2;

  const renderBoard = () => {
    const matrix = [];
    for (let rowIndex = 0; rowIndex < size + extra; rowIndex++) {
      const row = renderRow(rowIndex);
      matrix.push(<div key={rowIndex} className="row">{row}</div>);
    }

    return matrix;
  };

  const renderRow = (rowIndex) => {
    const row = [];
    for (let columnIndex = 0; columnIndex < size + extra; columnIndex++) {
      const cellState = getBoardState(rowIndex, columnIndex);
      row.push(
        <Cell
          key={`${rowIndex}-${columnIndex}`}
          state={cellState}
          // onClick={() => onCellClick(rowIndex, columnIndex)}
        />
      );
    }
    return row;
  };

  const getBoardState = (row, col) => {
    const isInsideBoard = (r, c) => r >= extraCells && r < size + extraCells && c >= extraCells && c < size + extraCells;
    const isAboveBoard = (r, c) => r >= (extraCells - 1) && r < extraCells && c >= extraCells && c < size + extraCells;
    const isBelowBoard = (r, c) => r >= size + extraCells && r <= size + extraCells && c >= extraCells && c < size + extraCells;
    const isLeftOfBoard = (r, c) => r >= extraCells && r < size + extraCells && c >= (extraCells - 1) && c < extraCells;
    const isRightOfBoard = (r, c) => r >= extraCells && r < size + extraCells && c >= size + extraCells && c <= size + extraCells;
  
    if (isInsideBoard(row, col)) {
      return boardState[row - extraCells][col - extraCells];
    } else if (isAboveBoard(row, col)) {
      return 'border-u';
    } else if (isBelowBoard(row, col)) {
      return 'border-d';
    } else if (isLeftOfBoard(row, col)) {
      return 'border-l';
    } else if (isRightOfBoard(row, col)) {
      return 'border-r';
    } else if (row === (extraCells - 1) && col === (extraCells - 1)) {
      return 'border-ul';
    } else if (row === (extraCells - 1) && col === size + extraCells) {
      return 'border-ur';
    } else if (row === size + extraCells && col === (extraCells - 1)) {
      return 'border-dl';
    } else if (row === size + extraCells && col === size + extraCells) {
      return 'border-dr';
    }
  
    return 'water';
  };

  return (
    <div className="board-render">
      {renderBoard()}
    </div>
  );
};
export default Board;
