====================
OHIS Line Compliance
====================
.. _OHIS_Line:

+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
|       Line        |PIN| Connected Board Nets      | Impedence |     Voltage     | Amperage | Notes                                                                                 |
+===================+===+===========================+===========+=================+==========+=======================================================================================+
| Power (+)         | 1 | OHIS Dedicated 5 volt (+) |    N/A    |     5 volts     |    1 A   |                                                                                       |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Power (-)         | 7 | OHIS (-)                  |    N/A    |     0 volts     |          |                                                                                       |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Headphone Left    | 4 | OHIS Headphone Left       |   8-64Ω   | -45dBV +/- 3dBV |          | Check Radio for Supported Ohms on Connection Used                                     |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Headphone Right   | 8 | OHIS Headphone Right      |   8-64Ω   | -45dBV +/- 3dBV |          | ^^^                                                                                   |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Headphone Ground  | 5 | OHIS Headphone Ground     |   8-64Ω   | -45dBV +/- 3dBV |          | ^^^                                                                                   |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Microphone Line   | 6 | OHIS Microphone Line      |    600Ω   |     5 volts     |  2.2 mA  | A DC block is in place to ensure that this is not dumped back to radio or accessories |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Microphone Ground | 3 | OHIS Microphone Ground    |    600Ω   |                 |          |                                                                                       |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| PTT Engage        | 2 | PTT Enable                |    N/A    |                 |          | Enable will come in the form of a short to OHIS (-)                                   |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
| Ethernet Ground   | S | Universal Ground Bond     |    N/A    |      Ground     |          |                                                                                       |
+-------------------+---+---------------------------+-----------+-----------------+----------+---------------------------------------------------------------------------------------+
