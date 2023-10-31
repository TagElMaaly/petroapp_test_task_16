# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrEmployeeTestTask(models.Model):
    _name = "hr.employee.test.task"
    _description = "Employee"
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'avatar.mixin']

    name = fields.Char(string="Employee Name", readonly=True)
    first_name = fields.Char(string="First Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    active = fields.Boolean(string="Active", default=True)

    @api.onchange('first_name', 'last_name')
    def _compute_employee_name(self):
        """
        This function compute the employee name onchange first name or the second name of the employee.
        :return:
        """
        for employee in self:
            employee.name = (employee.first_name or '') + " " + (employee.last_name or '')
