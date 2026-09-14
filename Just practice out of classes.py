# import pygame
# # y=(input("Enter numbers here:"))
# # x=(input("Enter numbers here:"))
# # print("x+y=", x+y)


# crash_sound = pygame.mixer.Sound("crash.wav")

                price = self.stationery_items[item] * rate
                cost = quantity * price
                total_cost += cost
 
                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price} = {symbol}{cost}\n"
                    )
 
        if total_cost > 0:
            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost}"
            )
 
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
 
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one stationery item."
            )
 
 
# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()
 
    app = StationeryOrderManagement(root)
 
    root.geometry("800x600")
 
    # Start the GUI event loop
    root.mainloop()
