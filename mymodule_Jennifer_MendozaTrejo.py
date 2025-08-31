# mymodule_Jennifer_MendozaTrejo.py

def pay_calculator(hourly_wage, regular_hours, overtime_hours):
      """Calculates employee's total weekly pay including overtime."""
      total_pay = (regular_hours * hourly_wage) + (overtime_hours * 1.5 * hourly_wage)

      return total_pay
