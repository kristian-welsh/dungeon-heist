
def within(small, target, large):
    return small <= target and target <= large

class Segment:
    def __init__(self, rect, rightSegments, bottomSegments):
        self.rect = rect
        self.rightSegments = rightSegments
        self.bottomSegments = bottomSegments

    def rights_for(self, new_rect):
        return [seg for seg in self.rightSegments if
                within(seg.rect.top, new_rect.top, seg.rect.bottom) or
                within(seg.rect.top, new_rect.bottom, seg.rect.bottom)]
        

    def downs_for(self, new_rect):
        return [seg for seg in self.bottomSegments if
                within(seg.rect.left, new_rect.left, seg.rect.right) or
                within(seg.rect.left, new_rect.right, seg.rect.right)]

    # creates rectangles to surround the position rectangle, top and bottom are wide
    def cut_rects(self, position, replaced):
        this = self.rect
        top = Rectangle(this.top, position.top, this.left, this.right)
        left = Rectangle(position.top, position.bottom, this.left, position.left)
        right = Rectangle(position.top, position.bottom, position.right, this.right)
        bottom = Rectangle(position.bottom, this.bottom, this.left, this.left),
        return (top, left, right, bottom)

    # replaces a segment with rect defined by pos_rect, with surrounding fillers
    def replace_segment(self, pos_rect, replaced):
        (top_rect, left_rect, right_rect, bottom_rect) = self.cut_rects(pos_rect, replaced.rect)

        bottom = Segment(
                bottom_rect,
                replaced.rights_for(bottom_rect),
                replaced.downs_for(bottom_rect))
        center_right = Segment(
                center_right_rect,
                replaced.rights_for(center_right_rect),
                [bottom])
        center_middle = Segment(
                pos_rect, 
                [center_right],
                [bottom])
        center_left = Segment(
                center_left_rect,
                [center_middle],
                [bottom])
        top = Segment(
                top_rect,
                replaced.rights_for(top_rect),
                [center_left, center_middle, center_right])
