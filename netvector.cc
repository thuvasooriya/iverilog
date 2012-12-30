/*
 * Copyright (c) 2012 Stephen Williams (steve@icarus.com)
 *
 *    This source code is free software; you can redistribute it
 *    and/or modify it in source code form under the terms of the GNU
 *    General Public License as published by the Free Software
 *    Foundation; either version 2 of the License, or (at your option)
 *    any later version.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with this program; if not, write to the Free Software
 *    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

# include  "netvector.h"

using namespace std;

netvector_t netvector_t::atom2s32 (IVL_VT_BOOL, 31, 0, true);
netvector_t netvector_t::atom2u32 (IVL_VT_BOOL, 31, 0, false);
netvector_t netvector_t::atom2s16 (IVL_VT_BOOL, 16, 0, true);
netvector_t netvector_t::atom2u16 (IVL_VT_BOOL, 16, 0, false);
netvector_t netvector_t::atom2s8  (IVL_VT_BOOL,  8, 0, true);
netvector_t netvector_t::atom2u8  (IVL_VT_BOOL,  8, 0, false);

netvector_t::netvector_t(ivl_variable_type_t type, long msb, long lsb, bool flag)
: type_(type), signed_(flag), isint_(false), is_scalar_(false)
{
      packed_dims_.push_back(netrange_t(msb,lsb));
}

netvector_t::netvector_t(ivl_variable_type_t type)
: type_(type), signed_(false), isint_(false), is_scalar_(false)
{
}

netvector_t::~netvector_t()
{
}

ivl_variable_type_t netvector_t::base_type() const
{
      return type_;
}

long netvector_t::packed_width() const
{
      return netrange_width(packed_dims_);
}

vector<netrange_t> netvector_t::slice_dimensions() const
{
      return packed_dims_;
}