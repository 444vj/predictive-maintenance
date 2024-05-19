import nbformat

def merge_notebook_cells(input_path, output_path):
    # Read the input notebook
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Extract code from each cell
    code_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'code']
    
    # Combine all code into a single string
    combined_code = '\n\n'.join(code_cells)
    
    # Create a new notebook
    new_nb = nbformat.v4.new_notebook()
    
    # Create a single code cell with the combined code
    new_code_cell = nbformat.v4.new_code_cell(combined_code)
    
    # Add the code cell to the new notebook
    new_nb.cells.append(new_code_cell)
    
    # Write the new notebook to the output path
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(new_nb, f)
        
    
    print(f"Merged notebook created at: {output_path}")

# Usage
input_notebook_path = r"C:\Users\jayshree v j\OneDrive\Desktop\code-crux\python\predictive-maintenance\predictive_maintenance.ipynb"
output_notebook_path = r"C:\Users\jayshree v j\OneDrive\Desktop\code-crux\python\predictive-maintenance\new_merged_notebook.ipynb"

merge_notebook_cells(input_notebook_path, output_notebook_path)

