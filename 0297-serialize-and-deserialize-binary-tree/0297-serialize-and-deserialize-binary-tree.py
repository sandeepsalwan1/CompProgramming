class Codec:

    def serialize(self, root):
        result = []
        # Helper function to perform preorder traversal
        
        def preorder(node):
            if not node:
                result.append("None")
                # Mark null nodes explicitly
                return
            result.append(str(node.val))
            # Add current node value to result
            preorder(node.left)
            # Recursively serialize left subtree
            preorder(node.right)
            # Recursively serialize right subtree
        
        preorder(root)
        # Start the serialization process
        return ",".join(result)
        # Join all values with commas to create the string

    def deserialize(self, data):
        if not data:
            return None
            # Handle empty string case
        
        values = data.split(",")
        # Split the string by commas to get individual node values
        self.index = 0
        # Initialize index to track position in values list
        
        def build():
            if self.index >= len(values) or values[self.index] == "None":
                self.index += 1
                # Move to next value
                return None
                # Return None for null nodes
            
            node = TreeNode(int(values[self.index]))
            # Create new node with current value
            self.index += 1
            # Move to next value
            node.left = build()
            # Recursively build left subtree
            node.right = build()
            # Recursively build right subtree
            return node
            # Return the constructed node
        
        return build()
        # Start the deserialization process
