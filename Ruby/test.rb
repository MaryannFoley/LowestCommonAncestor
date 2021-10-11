require_relative 'lca'
require 'test/unit'

class LCATest < Test::Unit::TestCase
  def setup
  	@root = Node.new("Root")
	@right = Node.new("R")
	@left = Node.new("L")
	@leftright = Node.new("LR")
	@leftleft = Node.new("LL")
	@leftleftright = Node.new("LLR")
	@rightleft = Node.new("RL")

	@root.left = @left
	@root.right = @right
	@left.right = @leftright
	@left.left = @leftleft
	@leftleft.right = @leftleftright
	@right.left = @rightleft
  end

  def test_same
    assert_equal(@left.print_data(), lowest_common_ancestor(@left,@left,@root))
  end

  def test_seperate
    assert_equal(@root.print_data(), lowest_common_ancestor(@right,@left,@root))
  end

  def test_seperate_swap
    assert_equal(@root.print_data(), lowest_common_ancestor(@left,@right,@root))
  end

  def test_parent
    assert_equal(@left.print_data(), lowest_common_ancestor(@leftleft,@left,@root))
  end

  def test_parent_right
    assert_equal(@leftleft.print_data(), lowest_common_ancestor(@leftleft,@leftleftright,@root))
  end

  def test_parents_parent
    assert_equal(@left.print_data(), lowest_common_ancestor(@leftleftright,@left,@root))
  end

end
