import streamlit as st
import numpy as np

# Function to validate if the Sudoku grid is valid
def is_valid_grid(grid):
    for i in range(9):
        # Check rows and columns for duplicates
        if len(set(grid[i])) != len([x for x in grid[i] if x != 0]):
            return False
        if len(set([grid[j][i] for j in range(9)])) != len([grid[j][i] for j in range(9) if grid[j][i] != 0]):
            return False
    
    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[row + i][col + j])
            if len(set(subgrid)) != len([x for x in subgrid if x != 0]):
                return False
    
    return True

# Function to display Sudoku grid and collect user input
def sudoku_game():
    st.title("Simple Sudoku Game")
    
    # Create an empty 9x9 Sudoku grid
    grid = np.zeros((9, 9), dtype=int)

    # Display the grid as input boxes
    for i in range(9):
        cols = st.columns(9)
        for j in range(9):
            grid[i][j] = cols[j].number_input(
                f"({i+1},{j+1})", min_value=0, max_value=9, key=f"{i}-{j}"
            )

    # Button to check if the Sudoku grid is valid
    if st.button("Check Sudoku"):
        if is_valid_grid(grid):
            st.success("Sudoku is valid!")
        else:
            st.error("Sudoku is not valid!")

# Run the Sudoku game
if __name__ == "__main__":
    sudoku_game()
