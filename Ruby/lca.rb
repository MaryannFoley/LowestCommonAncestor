#first attempt w ruby :-)
class Node
  attr_accessor :left
  attr_accessor :right

  def initialize(data)
    @data = data
  end

  def print_data()
    puts @data
  end

  def print_subtrees(indentation = "")
    if  !@right.nil?
      @right.print_subtrees(indentation + "\t")
    end
    if !@left.nil? || !@right.nil?
      puts indentation+@data+" ----"
    else
      puts indentation+@data
    end
    if  !@left.nil?
      @left.print_subtrees(indentation + "\t")
    end
    
  end
end



def lowest_common_ancestor (node1, node2, currentNode)
  if node1 == node2
    #puts node1.print_data 
    return currentNode.print_data
  else
    found = 0
    if !currentNode.left.nil?
      leftfound = lowest_common_ancestor(node1, node2, currentNode.left)
      if leftfound.instance_of? Fixnum
        found += leftfound
      else
        return leftfound
      end
    end

    if !currentNode.right.nil?
      rightfound = lowest_common_ancestor(node1, node2, currentNode.right)
      if rightfound.instance_of? Fixnum
        found += rightfound
      else
        return rightfound
      end
    end

    if rightfound == 2 || leftfound == 2
      return 2
    end

    if currentNode == node1 || currentNode == node2
      found += 1
    end

    if found == 2
      #puts currentNode.print_data
      return currentNode.print_data
    end

    return found
  end
end





# root = Node.new("Root")
# right = Node.new("R")
# left = Node.new("L")
# leftright = Node.new("LR")
# leftleft = Node.new("LL")
# leftleftright = Node.new("LLR")
# rightleft = Node.new("RL")

# root.left = left
# root.right = right
# left.right = leftright
# left.left = leftleft
# leftleft.right = leftleftright
# right.left = rightleft

# puts "\n"
# root.print_subtrees
