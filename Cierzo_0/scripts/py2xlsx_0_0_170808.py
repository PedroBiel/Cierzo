# -*- coding: utf-8 -*-


import os
import datetime
import xlsxwriter


def py2xlsx(name_xlsx, name_py, *args):
    """
    Creating Excel files with Python and XlsxWriter.

    Attributes:
    name_xlsx : Microsoft Excel file name.
    name_py   : Application name.
    *args     : Data.
    """

    # Create a new workbook and worksheet.

    workbook = xlsxwriter.Workbook(name_xlsx, {'strings_to_numbers': True, })
    workbook.set_properties({'title': 'Wind action',
                             'subject': 'according to FEM 2131/2132',
                             'author': 'Pedro Biel'})
    worksheet = workbook.add_worksheet('Wind action')

    # Format.

    format_titel = workbook.add_format()  # Titel.
    format_titel.set_bold()
    format_titel.set_font_size(14)

    format_project = workbook.add_format()  # Project.
    format_project.set_align('left')

    format_table = workbook.add_format()  # Table.
    format_table.set_align('center')

    format_units = workbook.add_format()  # Row of units.
    format_units.set_align('center')
    format_units.set_bottom(1)

    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 13)
    worksheet.set_column('D:D', 13)
    worksheet.set_column('E:E', 26)

    worksheet.hide_gridlines(2)  # Hide screen and printed grid lines.

    # Titel.

    worksheet.write('A1', 'Wind action according to FEM 2131/2132', format_titel)
    worksheet.write('A2', name_py)
    worksheet.write('A3', datetime.datetime.today().strftime('%Y.%m.%d %H:%M:%S'))

    # Project.

    worksheet.write('A5', 'Project:')
    worksheet.write('A6', 'Name:')
    worksheet.write('A7', 'Company:')
    worksheet.write('A8', 'Author:')
    worksheet.write('A9', 'Commentary:')

    worksheet.write('B5', args[0], format_project)
    worksheet.write('B6', args[1], format_project)
    worksheet.write('B7', args[2], format_project)
    worksheet.write('B8', args[3], format_project)
    worksheet.write('B9', args[4], format_project)

    if len(args) > 25:  # If the length of the args file is more than 25 the commentaries,
                        # field has more than one paragraph.

        extra_paragraphs = len(args) - 25
        row = 9
        col = 1

        for i in range(extra_paragraphs):
            worksheet.write(row + i, col, args[5 + i])
            i += 1

    # Wind action.

    worksheet.write('A14', 'Wind action')
    worksheet.write('A15', '', format_units)
    worksheet.write('A16', 'In service')
    worksheet.write('A17', 'Travelling to storm anchoring')
    worksheet.write('A18', 'Out of service (0 to 20 m)')
    worksheet.write('A19', 'Out of service (20 to 100 m)')
    worksheet.write('A20', 'Out of service (more than 100 m)')

    worksheet.write('B15', '', format_units)

    worksheet.merge_range('C14:D14', 'Design wind speed', format_table)
    worksheet.write('C15',           'm/s',               format_units)
    worksheet.write('D15',           'km/h',              format_units)

    worksheet.write('E14', 'Aerodynamic wind pressure', format_table)
    worksheet.write('E15', 'kN/m²',                     format_units)

    worksheet.write('F14', 'Ratio', format_table)
    worksheet.write('F15', '', format_units)

    worksheet.write('G14', '§', format_table)
    worksheet.write('G15', '', format_units)

    worksheet.write('C16', args[-20], format_table)
    worksheet.write('D16', args[-19], format_table)
    worksheet.write('E16', args[-18], format_table)
    worksheet.write('F16', args[-17], format_table)

    worksheet.write('C17', args[-16], format_table)
    worksheet.write('D17', args[-15], format_table)
    worksheet.write('E17', args[-14], format_table)
    worksheet.write('F17', args[-13], format_table)

    worksheet.write('C18', args[-12], format_table)
    worksheet.write('D18', args[-11], format_table)
    worksheet.write('E18', args[-10], format_table)
    worksheet.write('F18', args[-9],  format_table)

    worksheet.write('C19', args[-8], format_table)
    worksheet.write('D19', args[-7], format_table)
    worksheet.write('E19', args[-6], format_table)
    worksheet.write('F19', args[-5], format_table)

    worksheet.write('C20', args[-4], format_table)
    worksheet.write('D20', args[-3], format_table)
    worksheet.write('E20', args[-2], format_table)
    worksheet.write('F20', args[-1], format_table)

    worksheet.write('G16', '2-2.2.1', format_table)
    worksheet.write('G18', '2-2.3.6', format_table)
    worksheet.write('G19', '2-2.3.6', format_table)
    worksheet.write('G20', '2-2.3.6', format_table)

    # Footer.

    footer_left = '&L&6&"Monospac821 BT" &F / ' + os.path.basename(__file__) + ' / ' + args[3]
    footer_right = '&R&6&"Monospac821 BT" &P/&N'
    worksheet.set_footer(footer_left + footer_right)

    # Close workbook

    workbook.close()

    # Starts Excel

    #os.system(name_xlsx)


if __name__ == '__main__':

    data = ['12345', 'Estructuras', 'TAIM WESERs', 'Dr Nos', 'No comments 1.', 'No comments 2.', 'No 3.', 'No 4.',
            '20', '72', '0,25', '1,000',
            '28', '100', '0,48', '1,960',
            '36', '129', '0,79', '3,240',
            '42', '151', '1,08', '4,410',
            '46', '165', '1,30', '5,290'
            ]

    print(len(data))

    py2xlsx('qqq.xlsx', *data)
