# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, _next = nil)
      @val = val
      @next = _next
  end
end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
  prehead = ListNode.new
  p = prehead
  while !list1.nil? && !list2.nil?
      if list1.val > list2.val
          p.next = list2
          list2 = list2.next
      else list1.val <= list2.val
          p.next = list1
          list1 = list1.next
      end
      p = p.next
  end
  
  [list1,list2].each do |rn|
      if rn
          p.next = rn
          p = p.next
      end
  end
  
  return prehead.next
end