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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"T-Shirt Factory PRE ALPHA", pos = wx.DefaultPosition, size = wx.Size( 476,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		BoxSizer = wx.BoxSizer( wx.VERTICAL )

		InputLabelBox = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input" ), wx.VERTICAL )

		InputLabelBox.SetMinSize( wx.Size( -1,20 ) )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.UserIdLable = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Customer ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserIdLable.Wrap( -1 )

		gSizer1.Add( self.UserIdLable, 0, wx.ALL, 5 )

		UserIdComboBoxChoices = []
		self.UserIdComboBox = wx.ComboBox( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Customer ID", wx.DefaultPosition, wx.DefaultSize, UserIdComboBoxChoices, 0 )
		gSizer1.Add( self.UserIdComboBox, 0, wx.ALL, 5 )

		self.ClothingTypeLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Clothing Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ClothingTypeLabel.Wrap( -1 )

		gSizer1.Add( self.ClothingTypeLabel, 0, wx.ALL, 5 )

		ClothingTypeChoiceChoices = []
		self.ClothingTypeChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClothingTypeChoiceChoices, 0 )
		self.ClothingTypeChoice.SetSelection( 0 )
		gSizer1.Add( self.ClothingTypeChoice, 0, wx.ALL, 5 )

		self.ClothingSizeLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ClothingSizeLabel.Wrap( -1 )

		gSizer1.Add( self.ClothingSizeLabel, 0, wx.ALL, 5 )

		SizeChoiceChoices = []
		self.SizeChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SizeChoiceChoices, 0 )
		self.SizeChoice.SetSelection( 0 )
		gSizer1.Add( self.SizeChoice, 0, wx.ALL, 5 )

		self.ClothingColorLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ClothingColorLabel.Wrap( -1 )

		gSizer1.Add( self.ClothingColorLabel, 0, wx.ALL, 5 )

		ClothingColorChoiceChoices = []
		self.ClothingColorChoice = wx.Choice( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClothingColorChoiceChoices, 0 )
		self.ClothingColorChoice.SetSelection( 0 )
		gSizer1.Add( self.ClothingColorChoice, 0, wx.ALL, 5 )

		self.QuantitiesLabel = wx.StaticText( InputLabelBox.GetStaticBox(), wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.QuantitiesLabel.Wrap( -1 )

		gSizer1.Add( self.QuantitiesLabel, 0, wx.ALL, 5 )

		self.QuantitiesSpin = wx.SpinCtrl( InputLabelBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 80, 14 )
		gSizer1.Add( self.QuantitiesSpin, 0, wx.ALL, 5 )

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


		InputLabelBox.Add( gSizer1, 1, 0, 5 )


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

		OutputFormatChoiceChoices = []
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
		self.SetMenuBar( self.MenuBar )


		self.Centre( wx.BOTH )

		# Connect Events
		self.ExportButton.Bind( wx.EVT_BUTTON, self.export_all )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def export_all( self, event ):
		event.Skip()


