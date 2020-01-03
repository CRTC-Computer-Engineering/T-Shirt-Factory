# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class root_frame
###########################################################################

class root_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"T-Shirt Factory PRE ALPHA", pos = wx.DefaultPosition, size = wx.Size( 472,741 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		BoxSizer = wx.BoxSizer( wx.VERTICAL )

		InputLabelBox = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input" ), wx.VERTICAL )

		InputLabelBox.SetMinSize( wx.Size( -1,20 ) )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.UserIdLable = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Customer ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserIdLable.Wrap( -1 )

		gSizer1.Add( self.UserIdLable, 0, wx.ALL, 5 )

		UserIdComboBoxChoices = [ u"CustomerIDs" ]
		self.UserIdComboBox = wx.ComboBox( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Customer ID", wx.DefaultPosition, wx.DefaultSize, UserIdComboBoxChoices, 0 )
		gSizer1.Add( self.UserIdComboBox, 0, wx.ALL, 5 )

		self.ClothingTypeLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Clothing Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ClothingTypeLabel.Wrap( -1 )

		gSizer1.Add( self.ClothingTypeLabel, 0, wx.ALL, 5 )

		ClothingTypeChoiceChoices = []
		self.ClothingTypeChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClothingTypeChoiceChoices, 0 )
		self.ClothingTypeChoice.SetSelection( 0 )
		gSizer1.Add( self.ClothingTypeChoice, 0, wx.ALL, 5 )

		self.ClothingColorLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ClothingColorLabel.Wrap( -1 )

		gSizer1.Add( self.ClothingColorLabel, 0, wx.ALL, 5 )

		ClothingColorChoiceChoices = []
		self.ClothingColorChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClothingColorChoiceChoices, 0 )
		self.ClothingColorChoice.SetSelection( 0 )
		gSizer1.Add( self.ClothingColorChoice, 0, wx.ALL, 5 )

		self.BasePriceLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Base Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BasePriceLabel.Wrap( -1 )

		gSizer1.Add( self.BasePriceLabel, 0, wx.ALL, 5 )

		self.BasePriceInput = wx.TextCtrl( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"14.99", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.BasePriceInput, 0, wx.ALL, 5 )

		self.DiscountLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Discount", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DiscountLabel.Wrap( -1 )

		gSizer1.Add( self.DiscountLabel, 0, wx.ALL, 5 )

		DiscountChoiceChoices = []
		self.DiscountChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, DiscountChoiceChoices, 0 )
		self.DiscountChoice.SetSelection( 0 )
		gSizer1.Add( self.DiscountChoice, 0, wx.ALL, 5 )


		InputLabelBox.Add( gSizer1, 0, 0, 5 )

		SizeLabelBox = wx.StaticBoxSizer( wx.StaticBox( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Sizes" ), wx.VERTICAL )

		SizeGridSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.XS = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"XS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.XS.Wrap( -1 )

		SizeGridSizer.Add( self.XS, 0, wx.ALL, 5 )

		self.XSSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.XSSpin, 0, wx.ALL, 5 )

		self.S = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.S.Wrap( -1 )

		SizeGridSizer.Add( self.S, 0, wx.ALL, 5 )

		self.SSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.SSpin, 0, wx.ALL, 5 )

		self.M = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"M", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.M.Wrap( -1 )

		SizeGridSizer.Add( self.M, 0, wx.ALL, 5 )

		self.MSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.MSpin, 0, wx.ALL, 5 )

		self.L = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.L.Wrap( -1 )

		SizeGridSizer.Add( self.L, 0, wx.ALL, 5 )

		self.LSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.LSpin, 0, wx.ALL, 5 )

		self.XL = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"XL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.XL.Wrap( -1 )

		SizeGridSizer.Add( self.XL, 0, wx.ALL, 5 )

		self.XLSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.XLSpin, 0, wx.ALL, 5 )

		self.XXL = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"XXL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.XXL.Wrap( -1 )

		SizeGridSizer.Add( self.XXL, 0, wx.ALL, 5 )

		self.XXLSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.XXLSpin, 0, wx.ALL, 5 )

		self.XXXL = wx.StaticText( SizeLabelBox.GetStaticBox(), wx.ID_ANY, u"XXXL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.XXXL.Wrap( -1 )

		SizeGridSizer.Add( self.XXXL, 0, wx.ALL, 5 )

		self.XXXLSpin = wx.SpinCtrl( SizeLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99, 0 )
		SizeGridSizer.Add( self.XXXLSpin, 0, wx.ALL, 5 )


		SizeLabelBox.Add( SizeGridSizer, 0, wx.EXPAND, 5 )


		InputLabelBox.Add( SizeLabelBox, 1, wx.EXPAND, 5 )


		BoxSizer.Add( InputLabelBox, 0, 0, 5 )

		OutputLabelBox = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Output" ), wx.VERTICAL )

		gSizer11 = wx.GridSizer( 3, 2, 0, 0 )

		self.OutputDirLabel = wx.StaticText( OutputLabelBox.GetStaticBox(), wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OutputDirLabel.Wrap( -1 )

		gSizer11.Add( self.OutputDirLabel, 0, wx.ALL, 5 )

		self.OutputDirSelection = wx.DirPickerCtrl( OutputLabelBox.GetStaticBox(), wx.ID_ANY, u"None", u"Select a folder", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.DIRP_DEFAULT_STYLE )
		gSizer11.Add( self.OutputDirSelection, 0, wx.ALL, 5 )

		self.OutputDataTypeLabel = wx.StaticText( OutputLabelBox.GetStaticBox(), wx.ID_ANY, u"OutputFormat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OutputDataTypeLabel.Wrap( -1 )

		gSizer11.Add( self.OutputDataTypeLabel, 0, wx.ALL, 5 )

		OutputFormatChoiceChoices = [ u"txt", u"pdf" ]
		self.OutputFormatChoice = wx.Choice( OutputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, OutputFormatChoiceChoices, 0 )
		self.OutputFormatChoice.SetSelection( 0 )
		gSizer11.Add( self.OutputFormatChoice, 0, wx.ALL, 5 )

		self.ExportButton = wx.Button( OutputLabelBox.GetStaticBox(), wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.ExportButton, 0, wx.ALL, 5 )


		OutputLabelBox.Add( gSizer11, 0, 0, 5 )


		BoxSizer.Add( OutputLabelBox, 0, 0, 5 )


		self.SetSizer( BoxSizer )
		self.Layout()
		self.MenuBar = wx.MenuBar( 0 )
		self.MenuBarFile = wx.Menu()
		self.MenuBarExit = wx.MenuItem( self.MenuBarFile, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuBarFile.Append( self.MenuBarExit )

		self.MenuBar.Append( self.MenuBarFile, u"File" )

		self.SetMenuBar( self.MenuBar )


		self.Centre( wx.BOTH )

		# Connect Events
		self.ExportButton.Bind( wx.EVT_BUTTON, self.export_all )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def export_all( self, event ):
		event.Skip()


