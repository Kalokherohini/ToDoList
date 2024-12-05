from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Initialize Console for Rich Output
console = Console()

# Task List to Store To-Do Items
tasks = []

def display_menu():
    """Display the Main Menu."""
    console.print("\n[bold cyan]To-Do List Application[/bold cyan]", justify="center")
    console.print("[bold yellow]1.[/bold yellow] Add a Task")
    console.print("[bold yellow]2.[/bold yellow] View Tasks")
    console.print("[bold yellow]3.[/bold yellow] Mark Task as Complete")
    console.print("[bold yellow]4.[/bold yellow] Delete a Task")
    console.print("[bold yellow]5.[/bold yellow] Exit")

def add_task():
    """Add a Task to the List."""
    task = Prompt.ask("[green]Enter the task[/green]")
    tasks.append({"task": task, "status": "Incomplete"})
    console.print(f"[bold green]Task added:[/bold green] {task}")

def view_tasks():
    """View All Tasks."""
    if not tasks:
        console.print("[italic yellow]No tasks available. Add some![/italic yellow]")
        return
    
    table = Table(title="To-Do List", show_header=True, header_style="bold magenta")
    table.add_column("ID", justify="center")
    table.add_column("Task", justify="left")
    table.add_column("Status", justify="center")

    for i, task in enumerate(tasks, 1):
        table.add_row(str(i), task["task"], task["status"])
    
    console.print(table)

def mark_task_complete():
    """Mark a Task as Complete."""
    view_tasks()
    if not tasks:
        return
    
    task_id = Prompt.ask("[cyan]Enter the Task ID to mark as complete[/cyan]", default="0")
    task_id = int(task_id)
    
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["status"] = "Complete"
        console.print(f"[bold green]Task marked as complete:[/bold green] {tasks[task_id - 1]['task']}")
    else:
        console.print("[red]Invalid Task ID.[/red]")

def delete_task():
    """Delete a Task."""
    view_tasks()
    if not tasks:
        return
    
    task_id = Prompt.ask("[cyan]Enter the Task ID to delete[/cyan]", default="0")
    task_id = int(task_id)
    
    if 1 <= task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        console.print(f"[bold red]Task deleted:[/bold red] {removed_task['task']}")
    else:
        console.print("[red]Invalid Task ID.[/red]")

def main():
    """Main Function to Run the To-Do List Application."""
    while True:
        display_menu()
        choice = Prompt.ask("[bold magenta]Choose an option[/bold magenta]", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            console.print("[bold cyan]Goodbye! Happy organizing![/bold cyan]")
            break

if __name__ == "__main__":
    main()
