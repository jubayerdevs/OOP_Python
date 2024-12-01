# class Button:
#     def __init__(self, text):
#         self.text = text

    
#     def on_click(self):
#         print("Clicked!!")

    
# class ConfirmButton(Button):
#     def on_click(self):
#         #confirmOrder()
#         print("confirm button clicked!")

# class CancelButton(Button):
#     def on_click(self):
#         #cancel_action()
#         print("Cancel butto clicked!")

# btn1 = ConfirmButton("OK")



class Polygon:
    #method to render a shape
    def render(self):
        print("Rendering Ploygon...")


class Square(Polygon):
    #renders square
    def render(self):
        print("Rendering Square...")



class Circle(Polygon):
    #renders circle
    def render(self):
        print("Rendering Circle...")


#create an object of Square
s1 = Square()
s1.render()

#create an object of circle
c1 = Circle()
c1.render()


