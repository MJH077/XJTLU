class TreeNode:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.children = []

    def make_decision(self, data):
        if not self.children:
            return self.data
        else:
            if data[self.key] == self.data:
                return self.children[0].make_decision(data)
            elif data[self.key] == "High or Medium" and self.key == "Income":
                return self.children[1].make_decision(data)
            elif data[self.key] == "Divorced" and self.key == "Marital Status":
                return self.children[1].make_decision(data)
            elif data[self.key] == "Single" and self.key == "Marital Status":
                return self.children[2].make_decision(data)
            else:
                return "No Decision"  # Handle cases where the data doesn't match the decision tree


# Create the decision tree using the provided list structure
decision_tree = TreeNode("Marital Status", "Marital Status")
decision_tree.children = [
    TreeNode("Married", "Married"),
    TreeNode("Not Married", "Married")
]
decision_tree.children[0].children = [
    TreeNode("Income", "Income"),
    TreeNode("Other", "Income")
]
decision_tree.children[0].children[0].children = [
    TreeNode("Medium", "Income"),
    TreeNode("Other", "Income")
]
decision_tree.children[1].children = [
    TreeNode("Income", "Income"),
    TreeNode("Single", "Marital Status")
]
decision_tree.children[1].children[0].children = [
    TreeNode("Low", "Income"),
    TreeNode("High or Medium", "Income")
]
decision_tree.children[1].children[0].children[1].children = [
    TreeNode("Marital Status", "Marital Status"),
    TreeNode("Single", "Marital Status"),
    TreeNode("Age", "Marital Status")
]
decision_tree.children[1].children[0].children[1].children[0].children = [
    TreeNode("Divorced", "Marital Status"),
    TreeNode("Single", "Marital Status")
]
decision_tree.children[1].children[0].children[1].children[0].children[0].children = [
    TreeNode("Income", "Income"),
    TreeNode("Other", "Income")
]
decision_tree.children[1].children[0].children[1].children[0].children[0].children[0].children = [
    TreeNode("High", "Income"),
    TreeNode("Other", "Income")
]
decision_tree.children[1].children[0].children[1].children[2].children = [
    TreeNode("Age", "Age"),
    TreeNode("Age", "Age")
]
decision_tree.children[1].children[0].children[1].children[2].children[1].children = [
    TreeNode(" <= 35 ", "Age"),
    TreeNode(" > 35 ", "Age")
]

# Example usage: Make a decision using input data
input_data = {
    "Marital Status": "Not Married",
    "Income": "Low"
}
result = decision_tree.make_decision(input_data)

# This will print 'Yes' or 'No' indicating the decision
print(result)
