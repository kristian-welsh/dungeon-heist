from src.main.rect import Rectangle

def within(small, target, large):
    return small <= target and target <= large

class Segment:
    def __init__(self, rect, rightSegments, bottomSegments):
        self.rect = rect
        self.rightSegments = rightSegments
        self.bottomSegments = bottomSegments
    # passes through right facing connections that could connect to new rect
    def rights_for(self, new_rect):
        return [seg for seg in self.rightSegments if
                within(seg.rect.top, new_rect.top, seg.rect.bottom) or
                within(seg.rect.top, new_rect.bottom, seg.rect.bottom)]
        
    # passes through facing connections that could connect to new rect
    def downs_for(self, new_rect):
        return [seg for seg in self.bottomSegments if
                within(seg.rect.left, new_rect.left, seg.rect.right) or
                within(seg.rect.left, new_rect.right, seg.rect.right)]

    # creates rectangles to surround the position rectangle, top and bottom are wide
    def cut_rects(self, position):
        this = self.rect
        top = Rectangle(this.top, position.top, this.left, this.right)
        left = Rectangle(position.top, position.bottom, this.left, position.left)
        right = Rectangle(position.top, position.bottom, position.right, this.right)
        bottom = Rectangle(position.bottom, this.bottom, this.left, this.right)
        return (top, left, right, bottom)

    # replaces a segment with rect defined by middle_rect, with surrounding fillers
    def replacements(self, middle_rect):
        (top_rect, left_rect, right_rect, bottom_rect) = self.cut_rects(middle_rect)

        bottom = Segment(
                bottom_rect,
                self.rights_for(bottom_rect),
                self.downs_for(bottom_rect))
        right = Segment(
                right_rect,
                self.rights_for(right_rect),
                [bottom])
        middle = Segment(
                middle_rect, 
                [right],
                [bottom])
        left = Segment(
                left_rect,
                [middle],
                [bottom])
        top = Segment(
                top_rect,
                self.rights_for(top_rect),
                [left, middle, right])

        return (top, left, middle, right, bottom)
